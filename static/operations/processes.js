const { createApp } = Vue;

createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            processes_online: [],
            processes: [],
            name: '',
            url: '',
            timeout: '',
            submit: false,
            id: 0
        }
    },
    mounted: function () {
        if (typeof list !== "undefined" && list == true) {
            this.listProcesses();
        }
        if (typeof load_process !== "undefined" && load_process > 0) {
            this.loadProcess(load_process);
        }
    },
    methods: {
        listProcesses: function () {
            axios
                .get(backend_url + "/processes")
                .then(response => {
                    var data = response.data;
                    var estado = data.estado;

                    if (estado == 1) {
                        var procesos = data.datos;
                        this.processes = procesos;
                        console.log('procesos', this.processes);
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })


            axios
                .get(backend_url + "/logs")
                .then(response => {
                    var data = response.data;
                    var estado = data.estado;

                    if (estado == 1) {
                        var logs = data.datos;
                        logs.forEach(log => {
                            this.processes_online.push(log.process_id);
                        });
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })

        },
        loadProcess: function (id) {
            axios
                .get(backend_url + "/processes/" + id)
                .then(response => {
                    var data = response.data;
                    var estado = data.estado;

                    if (estado == 1) {
                        var proceso = data.datos;
                        this.name = proceso.name;
                        this.url = proceso.url;
                        this.timeout = proceso.timeout;
                        this.id = id;
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })
        },
        save() {

            if (this.name && this.url && this.timeout) {

                const datos = {
                    "name": this.name,
                    "url": this.url,
                    "timeout": this.timeout
                };

                if (this.id > 0) {

                    axios
                        .put(backend_url + "/processes/" + this.id, datos)
                        .then(response => {

                            var data = response.data;

                            var status = data.estado;
                            var message = data.mensaje;

                            if (status == 1) {

                                Swal.fire({
                                    text: message,
                                    icon: 'success',
                                    confirmButtonText: 'Continuar'
                                }).then(function () {
                                    window.location = "/dashboard/procesos";
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

                    axios
                        .post(backend_url + "/processes", datos)
                        .then(response => {

                            var data = response.data;

                            var status = data.estado;
                            var message = data.mensaje;

                            if (status == 1) {

                                Swal.fire({
                                    text: message,
                                    icon: 'success',
                                    confirmButtonText: 'Continuar'
                                }).then(function () {
                                    window.location = "/dashboard/procesos";
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

                }

            } else {
                this.submit = true;
            }

        },
        remove() {

            if (this.id > 0) {

                axios
                    .delete(backend_url + "/processes/" + this.id)
                    .then(response => {

                        var data = response.data;

                        var status = data.estado;
                        var message = data.mensaje;

                        if (status == 1) {

                            Swal.fire({
                                text: message,
                                icon: 'success',
                                confirmButtonText: 'Continuar'
                            }).then(function () {
                                window.location = "/dashboard/procesos";
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
        start_process(id) {

            axios
                .get(backend_url + "/launcher/process/" + id + "/start")
                .then(response => {

                    var data = response.data;

                    var status = data.estado;
                    var message = data.mensaje;

                    if (status == 1) {

                        this.processes_online.push(id);

                        Swal.fire({
                            text: message,
                            icon: 'success',
                            confirmButtonText: 'Continuar'
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

        },
        stop_process(id) {

            axios
                .get(backend_url + "/launcher/process/" + id + "/stop")
                .then(response => {

                    var data = response.data;

                    var status = data.estado;
                    var message = data.mensaje;

                    if (status == 1) {

                        const list_processes = this.processes_online;

                        this.processes_online = list_processes.filter(function (e) { return e !== id });

                        Swal.fire({
                            text: message,
                            icon: 'success',
                            confirmButtonText: 'Continuar'
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

        }
    }
}).mount("#appProcesos");