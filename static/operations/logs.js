const { createApp } = Vue;

createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            logs: [],
            id: 0,
            pid: '',
            details: '',
            task_id: 0,
            process_id: 0
        }
    },
    mounted: function () {
        if (typeof list !== "undefined" && list == true) {
            this.listLogs();
        }
        if (typeof load_logs !== "undefined" && load_logs > 0) {
            this.loadLogs(load_logs);
        }
    },
    methods: {
        listLogs: function () {
            axios
                .get(backend_url + "/logs")
                .then(response => {
                    var data = response.data;
                    var estado = data.estado;

                    if (estado == 1) {
                        var logs = data.datos;
                        this.logs = logs;
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })
        },
        loadLogs: function (id) {
            axios
                .get(backend_url + "/logs/" + id)
                .then(response => {
                    var data = response.data;
                    var estado = data.estado;

                    if (estado == 1) {
                        var logs = data.datos;
                        this.id = id;
                        this.process_id = logs.process_id;
                        this.task_id = logs.task_id;
                        this.pid = logs.pid;
                        this.details = logs.logs;
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })
        },
        closeTask() {

            axios
                .get(backend_url + "/launcher/task/" + this.task_id + "/stop")
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
                            window.location = "/dashboard/logs";
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
        closeProcess() {

            axios
                .get(backend_url + "/launcher/process/" + this.process_id + "/stop")
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
                            window.location = "/dashboard/logs";
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
}).mount("#appLogs");