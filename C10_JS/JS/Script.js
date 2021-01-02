function perguntar() {
    var nome;
    nome = prompt("Digite seu nome:")
    alert("Olá " + nome)
}

function muda_nome(){
    var h1;
    h1 = document.getElementsByTagName('h1')
    if (h1[0].innerText == "Olá Mundinho Lindo") {
        h1[0].innerText = "Tchau Mundinho Lindo"
    }else{
        h1[0].innerText = "Olá Mundinho Lindo"
    }
}

function incrementar() {
    var p1;
    p1 = document.getElementById('p1')
    p1.innerText = parseInt(p1.innerText) + 1
}