
    
$(document).ready(function(){
    $('#botoncajas').on('click', function(){
        console.log(document.getElementById('botoncajas'));
        if(document.getElementById("p1texto").value==""){
                document.getElementById("p1").style.color="red";
        }
        if(document.getElementById("p2texto").value==""){
                document.getElementById("p2").style.color="red";
            }  
            if(document.getElementById("p1texto").value!="" && document.getElementById("p2texto").value!=""){
                window.location.href="/ejercicio3/solicita_pedido.html";
            }
    })
    $("#tamanno").on('change', function() {
        
        valor=document.getElementById("tamanno").value
        $.ajax({
            type: "POST",
            url: "http://localhost:5000/checksize",
            data: {
            "size": valor
            
            },
            success: function (result) {
                $("#resultado_tamano").text(result).value;
            }
            })
            
       });
})




    
        
    
    


