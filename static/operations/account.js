const { createApp } = Vue;

createApp({
    data() {
        return {
            usuario: '',
            nuevo_usuario: '',
            clave: '',
            nueva_clave: '',
            submit: false,
        }
    },
    methods: {
        save() {

            if (this.usuario && this.nuevo_usuario && this.clave && this.nueva_clave) {

                const datos = {
                    "username": this.usuario,
                    "new_username": this.nuevo_usuario,
                    "password": this.clave,
                    "new_password": this.nueva_clave
                }

                axios
                    .post(backend_url + "/account", datos)
                    .then(response => {

                        var data = response.data;

                        var status = data.estado;
                        var message = data.mensaje;

                        if (status == 1) {

                            sessionStorage.setItem(session_name, '');

                            Swal.fire({
                                text: message,
                                icon: 'success',
                                confirmButtonText: 'Continuar'
                            }).then(function () {
                                window.location = "/dashboard/salir";
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
}).mount("#appCuenta");