
/**/ /*
    $(document).ready(function () {	
    $("#artistas").click(function (e) { 
        e.preventDefault();
        $("#listaartistas").html('');
        $.get("js/artistas.json", function(data){
            console.log(data);
            $.each(data, function(index,value){
                $("#listaartistas").html($('#listaartistas').html()+`
                <li> ${value.nombre} ${value.apellido}</li>
                <li> ${value.email}</li>
                <li> ${value.telefono}</li>
                <li>${value.area}</li>
                 <br>    
                `);
            })
        })
    }); 
*/
/*$.get("js/artistas.json", function(data){ */

    $(document).ready(function () {  
        $("#artistas").click(function (e) { 
          e.preventDefault();
          $("#listaartistas").html('');
          
          $.get("js/artistas.json", function(data){
            console.log(data);
            $.each(data, function(index,value){
              $("#listaartistas").append(`
                <div>
                <ul>
                  <li>${value.nombre} ${value.apellido}</li>
                  <li>${value.email}</li>
                  <li>${value.telefono}</li>
                  <li>${value.area}</li>
                  </ul>
                </div>
              `);
            })
          })
        });
/* primera opcion 
    $('#nombre').keyup(function (e) { 
        let nombre=$(this).val();
        if(nombre.length === 0) {
            $('#listaartistas').empty();
            return;
        }
        $('#listaartistas').empty();
        $.get("js/artistas.json", function(data){
            $.each(data, function(indexInArray, item) {
                if(item.nombre.indexOf(nombre)!==-1){
                    $('#listaartistas').append(`
                        <li>Nombre: ${item.nombre} ${item.apellido}</li>
                        <li>Correo: ${item.email}</li>
                        <br>    
                    `);
                }
            })   
        });
    });
    */


    $('#nombre').keyup(function (e) { 
        
        let nombre=$(this).val();
        if(nombre.length === 0) {
            $('#listaartistas').empty();
            return;
        }
        $.get("js/artistas.json", function(data){
            $.each(data, function(indexInArray, item) {
                if(item.nombre.indexOf(nombre)!==-1){
                    $('#listaartistas').html(`
                        <li>Nombre: ${item.nombre} ${item.apellido}</li>
                        <li>Correo: ${item.email}</li>
                        <li>Numero: ${item.telefono}</li>
                        <li>Area:   ${item.area}</li>
                        <br>    
                    `);
                }
               
            })   
        });

     });
     
});


$(document).ready(function() {
    $("#artistas").click(function() {
      $(".alert").show();
    });
  });