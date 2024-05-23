document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault(); 
        
        var nombre = document.getElementById('nombre').value;
        var correo = document.getElementById('correo').value;
        var asunto = document.getElementById('asunto').value;
        var mensaje = document.getElementById('mensaje').value;

        if (!nombre || !correo || !asunto || !mensaje) {
            alert('Por favor, completa todos los campos.');
        } else {
            alert('Tu consulta se envió correctamente. Nos estaremos comunicando con vos en breve');
            document.getElementById('nombre').value="";
            document.getElementById('correo').value="";
            document.getElementById('asunto').value="";
            document.getElementById('mensaje').value="";
        }
    });
});