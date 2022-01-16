
    
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
})

    
        
    
    


