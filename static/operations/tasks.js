const { createApp } = Vue;

createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            tasks: [],
            name: '',
            directory: '',
            command: '',
            process_id: '',
            process_name: '',
            submit: false,
            id: 0
        }
    },
    mounted: function () {
        if (typeof list !== "undefined" && list == true) {
            this.listTasks();
        }
        if (typeof load_tasks_by_process !== "undefined" && load_tasks_by_process > 0) {
            this.listTasksByProcess(load_tasks_by_process);
        }
        if (typeof load_task !== "undefined" && load_task > 0) {
            this.loadTask(load_task);
        }
        if (typeof process_task !== "undefined" && process_task > 0) {
            this.process_id = process_task;
        }
    },
    methods: {
        listTasks: function () {
            axios
                .get(backend_url + "/tasks")
                .then(response => {
                    var data = response.data;
                    var estado = data.estado;

                    if (estado == 1) {
                        var tareas = data.datos;
                        this.tasks = tareas;
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })
        },
        listTasksByProcess: function (id) {
            axios
                .get(backend_url + "/processes/" + id + "/tasks")
                .then(response => {
                    var data = response.data;
                    var estado = data.estado;

                    if (estado == 1) {
                        var tareas = data.datos.tasks;
                        this.tasks = tareas;
                        this.process_name = data.datos.process.name;
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })
        },
        loadTask: function (id) {
            axios
                .get(backend_url + "/tasks/" + id)
                .then(response => {
                    var data = response.data;
                    var estado = data.estado;

                    if (estado == 1) {
                        var tarea = data.datos;
                        this.name = tarea.name;
                        this.directory = tarea.directory;
                        this.command = tarea.command;
                        this.id = id;
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })
        },
        save() {

            if (this.name && this.directory && this.command) {

                const datos = {
                    "name": this.name,
                    "directory": this.directory,
                    "command": this.command,
                    'process_id': this.process_id
                };

                if (this.id > 0) {

                    axios
                        .put(backend_url + "/tasks/" + this.id, datos)
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
                                    window.location = "/dashboard/procesos/" + process_task + "/tareas";
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
                        .post(backend_url + "/tasks", datos)
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
                                    window.location = "/dashboard/procesos/" + process_task + "/tareas";
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
                    .delete(backend_url + "/tasks/" + this.id)
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
                                window.location = "/dashboard/procesos/" + process_task + "/tareas";
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

        }
    }
}).mount("#appTareas");