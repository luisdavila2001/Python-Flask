from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
import requests


app=Flask(__name__, static_url_path='/static', static_folder='static')


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='CineStar'

conexion= MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cines')
def cines():
    try:
        cursor=conexion.connection.cursor()
        sql='call sp_getCines()'
        cursor.execute(sql)
        cines = cursor.fetchall()
    except Exception as exept:
        return 'Horror'
    return render_template('cines.html', cines = cines)

@app.route('/cine/<id>')
def cine(id):
    try:
        flecha = conexion.connection.cursor()
        sql='call sp_getCine(%s)' % id
        flecha.execute(sql)
        cine = flecha.fetchall()

        flecha = conexion.connection.cursor()
        sql='call sp_getCineTarifas(%s)' % id
        flecha.execute(sql)
        tarifas = flecha.fetchall()

        flecha = conexion.connection.cursor()
        sql='call sp_getCinePeliculas(%s)' % id
        flecha.execute(sql)
        cinepelicula = flecha.fetchall()
    except Exception as exept:
        return 'Horror'
    return render_template('cine.html', cine = cine, tarifas = tarifas, cinepelicula = cinepelicula)

@app.route('/peliculas/<id>')
def peliculas(id):
    try:
        flecha = conexion.connection.cursor()
        if id =='cartelera':
            sql ='call sp_getPeliculas(1)'
        else:
            sql ='call sp_getPeliculas(2)'
        flecha.execute(sql)
        peliculas = flecha.fetchall()
    except Exception as exept:
        return 'Eror'
    return render_template('peliculas.html', peliculas=peliculas)

@app.route('/pelicula/<id>')
def pelicula(id):
    try:
        flecha = conexion.connection.cursor()
        sql = 'call sp_getPelicula(%s)' % id
        flecha.execute(sql)
        pelicula = flecha.fetchall()
    except Exception as exept:
        return 'Error'
    return render_template('pelicula.html', pelicula = pelicula)


#apis

@app.route('/ciness')
def ciness():
    try:
        flecha = conexion.connection.cursor()
        sql = 'call sp_getCines()'
        flecha.execute(sql)
        cines = flecha.fetchall()
        data=[]
        for row in cines:
            cine={'id': row[0], 'RazonSocial': row[1], 'Salas': row[2], 'idDistrito': row[3], 'Direccion': row[4], 'Telefonos': row[5], 'Detalle': row[6]} 
            data.append(cine)
        
    except Exception as ex:
        data['mensaje']='Erro'
    return jsonify({'data': data})

if __name__=='__main__':
    app.run(debug=True)