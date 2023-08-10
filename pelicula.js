const getPelicula=async()=>{
  let id=(new URLSearchParams(window.location,search)).get('id')

  const data= await fetch(`http://localhost/cinestar_sweb_php/peliculas/${id}`)
    if(data.status==200){
        const peliculas =await data.json()
        let html=`<br/><h1>Cartelera</h1><br/>`

        peliculas.forEach(pelicula =>{
            html+=`
                    <div class="contenido-pelicula">
                        <div class="datos-pelicula">
                            <h2>${pelicula.Titulo}</h2>
                            <p>${pelicula.Sinopsis}</p>
                            <br/>
                            <div class="tabla">
                                <div class="fila">
                                    <div class="celda-titulo">Título Original :</div>
                                    <div class="celda">Jumanji: En la Selva (Todo Público)</div>
                                </div>
                                <div class="fila">
                                    <div class="celda-titulo">Estreno :</div>
                                    <div class="celda">11 de Enero del 2018</div>
                                </div>
                                <div class="fila">
                                    <div class="celda-titulo">Género :</div>
                                    <div class="celda">Aventura / Acción</div>
                                </div>
                                <div class="fila">
                                    <div class="celda-titulo">Director :</div>
                                    <div class="celda">Jake Kasdan</div>
                                </div>
                                <div class="fila">
                                    <div class="celda-titulo">Reparto :</div>
                                    <div class="celda">Dwayne Johnson, Kevin Hart, Jack Black, Karen Gillan</div>
                                </div>
                            </div>
                        </div>
                        <img src="img/pelicula/1.jpg" width="160" height="226"><br/><br/>
                    </div>
                    <div class="pelicula-video">
                        <embed src="https://www.youtube.com/v/${pelicula.Link}" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="580" height="400">
                    </div>
             `
      });
      document.getElementsById('contenido-interno').innerHTML=html
    }
}

getpelicula()



				