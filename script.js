function adicionarProduto() { // alteração
    const form = document.getElementById('productForm');
    const tabelaBody = document.getElementById('produtosTable').getElementsByTagName('tbody')[0];

    const codigo = form.codigo.value;
    const marca = form.marca.value;
    const tipo = form.tipo.value;
    const categoria = form.categoria.value;
    const preco = form.preco.value;
    const custo = form.custo.value;
    const observacoes = form.observacoes.value;

    const novaLinha = tabelaBody.insertRow(); // alteração

    novaLinha.innerHTML = `
        <td>${codigo}</td>
        <td>${marca}</td>
        <td>${tipo}</td>
        <td>${categoria}</td>
        <td>${preco}</td>
        <td>${custo}</td>
        <td>${observacoes}</td>
    `;

    form.reset(); // Limpa o formulário após adicionar o produto
}
document.addEventListener('DOMContentLoaded', (event) => { // alteração
    const inputs = document.querySelectorAll('input');
    inputs.forEach((input, index) => {
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                const nextInput = inputs[index + 1];
                if (nextInput) {
                    nextInput.focus();
                } else {
                    document.querySelector('button').click();
                }
            }
        });
    });
});