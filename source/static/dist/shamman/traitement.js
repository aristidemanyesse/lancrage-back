$(function () {

    var token = $("div.token input[type=hidden]").val();

    $("body").on("submit", "form.formShamman", function (event) {
        Loader.start()
        form = $(this).attr('classname');
        reload = $(this).attr('reload');
        url = "/core/ajax/save/";
        var formdata = new FormData($(this)[0]);
        formdata.append('modelform', form);
        if (form == "ProduitForm") {
            var infos = $('.summernote#infos').summernote('code');
            formdata.append('infos', infos);
            var avis = $('.summernote#avis').summernote('code');
            formdata.append('avis', avis);
            var recettes = $('.summernote#recettes').summernote('code');
            formdata.append('recettes', recettes);
            var faq = $('.summernote#faq').summernote('code');
            formdata.append('faq', faq);
        }
        $.post({ url: url, data: formdata, contentType: false, processData: false }, function (data) {
            if (data.status) {
                if (reload == "false") {
                    Loader.stop();
                    Alerter.success('Réussite', data.message);
                    $(".modal").modal('hide');
                } else if (!!data.url) {
                    window.location.href = data.url;
                } else {
                    window.location.reload();
                }
            } else {
                Alerter.error('Erreur !', data.message);
            }
        }, 'json')
        return false;
    });



    $("input.maj, select.maj").change(function () {
        url = "/core/ajax/mise_a_jour/";
        var val = $(this).val()
        var formdata = new FormData();
        formdata.append('id', $(this).attr("id"));
        formdata.append('modelform', $(this).attr("model"));
        formdata.append('name', $(this).attr("name"));
        formdata.append('val', $(this).val());
        formdata.append('csrfmiddlewaretoken', token);
        $.post({ url: url, data: formdata, contentType: false, processData: false }, function (data) {
            if (data.status) {
                Alerter.success('Reussite !', "Modification prise en compte avec succès !");
            } else {
                Alerter.error('Erreur !', data.message);
            }
        }, 'json')
    })


    filtrer = function () {
        Loader.start()
        session("date1", $("#formFiltrer input[name=date1]").val())
        window.location.reload();
    }


    filter_date = function (debut, fin) {
        url = "/core/ajax/filter_date/";
        Loader.start()
        $.post(url, { debut: debut, fin: fin }, (data) => {
            window.location.reload();
        }, "json");
    }


    enable = function (table, id) {
        url = "../../composants/dist/shamman/traitement.php";
        alerty.confirm("Voulez-vous changer la disponible de cet element ?", {
            title: "Changement de disponibilité",
            cancelLabel: "Non",
            okLabel: "OUI, Changer",
        }, function () {
            Loader.start()
            $.post(url, { action: "enable", table: table, id: id }, (data) => {
                if (data.status) {
                    window.location.reload()
                } else {
                    Alerter.error('Erreur !', data.message);
                }
            }, "json");
        })
    }



    annuler = function (table, id) {
        url = "../../composants/dist/shamman/traitement.php";
        alerty.confirm("Voulez-vous vraiment annuler cet element ?", {
            title: "Annulation // suppression",
            cancelLabel: "Non",
            okLabel: "OUI, annuler",
        }, function () {
            alerty.prompt("Entrer votre mot de passe pour confirmer l'opération !", {
                title: 'Récupération du mot de passe !',
                inputType: "password",
                cancelLabel: "Annuler",
                okLabel: "Valider"
            }, function (password) {
                Loader.start();
                $.post(url, { action: "annuler", table: table, id: id, password: password }, (data) => {
                    if (data.status) {
                        window.location.reload()
                    } else {
                        Alerter.error('Erreur !', data.message);
                    }
                }, "json");
            })
        })
    }


    change_active = function (model, id) {
        url = "/core/ajax/change_active/";
        $.post(url, { model: model, id: id }, (data) => {
            if (data.status) {
                Alerter.success('Mise à jour !', "Modification effectuée avec succès !");
            } else {
                Alerter.error('Erreur !', data.message);
            }
        }, "json");
    }



    supprimer = function (model, id) {
        url = "/core/ajax/supprimer/";
        alerty.confirm("Voulez-vous vraiment supprimer cet element ?", {
            title: "Suppression",
            cancelLabel: "Non",
            okLabel: "OUI, supprimer",
        }, function () {
            Loader.start();
            var formdata = new FormData();
            formdata.append('id', id);
            formdata.append('model', model);
            formdata.append('csrfmiddlewaretoken', token);
            $.post({ url: url, data: formdata, contentType: false, processData: false }, function (data) {
                if (data.status) {
                    window.location.reload()
                } else {
                    Alerter.error('Erreur !', data.message);
                }
            }, 'json')
        })
    }


    delete_password = function (model, id) {
        url = "/core/ajax/supprimer/";
        alerty.confirm("Voulez-vous vraiment supprimer cet element ?", {
            title: "Suppression",
            cancelLabel: "Non",
            okLabel: "OUI, supprimer",
        }, function () {
            alerty.prompt("Entrer votre mot de passe pour confirmer l'opération !", {
                title: 'Une dernière étape !',
                inputType: "password",
                cancelLabel: "Annuler",
                okLabel: "Valider"
            }, function (password) {
                Loader.start();
                var formdata = new FormData();
                formdata.append('id', id);
                formdata.append('model', model);
                formdata.append('password', password);
                formdata.append('csrfmiddlewaretoken', token);
                $.post({ url: url, data: formdata, contentType: false, processData: false }, function (data) {
                    if (data.status) {
                        window.location.reload()
                    } else {
                        Alerter.error('Erreur !', data.message);
                    }
                }, 'json')
            })
        })
    }

})