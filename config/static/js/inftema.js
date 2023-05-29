
function cargarNivel() {
    const selectNivel = document.getElementById("selinftema-nivel");

    let endpoint2 = "/consultanivel";
    axios
        .get(endpoint2)
        .then(function (response) {
            // La datos contiene los datos devueltos por la API
            const datos = response.data;

            // Iterar sobre los datos y agregar opciones al select
            for (let key in datos) {
                const option = document.createElement("option");
                option.text = datos[key].nombre_nv;
                selectNivel.appendChild(option);
            }
        })
        .catch(function (error) {
            console.error(error);
        });

}
function cargarTematica2() {
    const selectIdtema = document.getElementById("selinftema-id");
    let endpoint = "/consultatematica";
    axios
        .get(endpoint)
        .then(function (response) {
            // La datos contiene los datos devueltos por la API
            const datos = response.data;
            // Iterar sobre los datos y agregar opciones al select
            for (let key in datos) {
                const option = document.createElement("option");
                option.text = datos[key].nombre_tematica;
                selectIdtema.appendChild(option);


            }
        })
        .catch(function (error) {
            console.error(error);
        });
}

var idTematicaG = "";
var idNivelG = "";

function saveinftema2() {
    const TituloInf = document.getElementById("Tituloinf").value;
    const DescripcionInf = document.getElementById("desc").value;
    const selectNivel = document.getElementById("selinftema-nivel").value;
    const selectIdtema = document.getElementById("selinftema-id").value;
    let idTematica = "0";
    let idNivel = "0";

    if (TituloInf == "" || DescripcionInf == "" || selectNivel == "Seleccionar" || selectIdtema == "Seleccionar") {
        alert("Todos los campos son obligatorios");
    } else {
        let urlT = "/consultatematica";
        axios
            .get(urlT, {
                params: {
                    nombre_tematica: selectIdtema
                }
            })
            .then((response) => {
                const tematicas = response.data;

                Object.values(tematicas).forEach((tematica) => {
                    if (tematica.nombre_tematica === selectIdtema) {
                        idTematica = tematica.id;
                        idTematicaG = idTematica;
                    }
                });

                // Llamar al método POST después de obtener el id de la temática
                postInftema();
            })
            .catch(function (error) {
                console.log(error);
            });

        let urlN = "/consultanivel";
        axios
            .get(urlN, {
                params: {
                    nombre_nv: selectNivel
                }
            })
            .then((response) => {
                const niveles = response.data;

                Object.values(niveles).forEach((nivel) => {
                    if (nivel.nombre_nv === selectNivel) {
                        idNivel = nivel.id;
                        idNivelG = idNivel;
                    }
                });

                // Llamar al método POST después de obtener el id del nivel
                postInftema();
            })
            .catch(function (error) {
                console.log(error);
            });

        // Método para realizar la solicitud POST
        function postInftema() {
            if (idTematicaG !== "" && idNivelG !== "") {
                let endpoint = "/saveinftema";
                axios
                    .post(endpoint, {
                        Titulo_inftem: TituloInf,
                        Det_inftema: DescripcionInf,
                        Idtematica_Fk: idTematicaG,
                        IdNivel_fk: idNivelG,
                    })
                    .then(function (response) {
                        alert(response);
                        document.getElementById("Tituloinf").value = "";
                        document.getElementById("desc").value = "";
                        document.getElementById("selinftema-nivel").value = "Seleccionar";
                        document.getElementById("selinftema-id").value = "Seleccionar";

                    })
                    .catch(function (error) {
                        console.log(error);
                    });

                alert("Cambios guardados exitosamente.");
            }
        }
    }
}


