document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#enviarBtn').addEventListener('click', function () {
      var formulario = document.querySelector('#contactoForm');
      var inputs = formulario.querySelectorAll('input, textarea');
  
      var formularioValido = true;
  
      // Orden de validación
      var campos = ['nombreApellido', 'telefono', 'correo', 'empresa', 'mensaje'];
  
      for (var i = 0; i < campos.length; i++) {
        var campo = campos[i];
        var input = formulario.querySelector('#' + campo);
  
        if (!input.checkValidity()) {
          formularioValido = false;
          input.classList.add('is-invalid');
          input.classList.remove('is-valid');
          input.reportValidity();
          break;
        } else {
          input.classList.remove('is-invalid');
          input.classList.add('is-valid');
        }
      }
  
      if (formularioValido) {
        formulario.submit();
      }
    });
  });
  