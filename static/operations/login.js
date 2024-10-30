const { createApp } = Vue;

createApp({
    data() {
        return {
            usuario: '',
            clave: '',
            submit: false,
            procesos: []
        }
    },
    methods: {
        login() {

            if (this.usuario && this.clave) {

                axios
                    .post(backend_url + "/login", { "username": this.usuario, "password": this.clave })
                    .then(response => {

                        var data = response.data;

                        var status = data.estado;
                        var message = data.mensaje;

                        if (status == 1) {

                            var token = data.datos;

                            sessionStorage.setItem(session_name, token);

                            Swal.fire({
                                text: message,
                                icon: 'success',
                                confirmButtonText: 'Continuar'
                            }).then(function () {
                                window.location = "/dashboard";
                            });

                        } else {

                            Swal.fire({
                                text: message,
                                icon: 'warning',
                                confirmButtonText: 'Continuar'
                            });

                        }
                    })
                    .catch(function (error) {
                        console.log(error);
                    })

            } else {
                this.submit = true;
            }

        },
    }
}).mount("#appIngreso");