const form = document.getElementById("livroForm");
const container = document.getElementById("livrosContainer");

const API_URL = "http://localhost:8080/itens";


form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const titulo = document.getElementById("titulo").value;
  const autor = document.getElementById("autor").value;
  const tipo = document.getElementById("tipo").value;

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({  titulo, autor, tipo }),
    });

    if (!res.ok) {
      const erro = await res.text();
      throw new Error(erro);
    }

    Swal.fire({
      title: '✅ Adicionado!',
      text: `Novo ${tipo} cadastrado: "${titulo}" por ${autor}`,
      icon: 'success',
      timer: 2000,
      showConfirmButton: false
    });

    form.reset();
    carregarItens();
  } catch (err) {
    Swal.fire("❌ Erro ao adicionar", err.message, "error");
    console.error(err);
  }
});


async function carregarItens() {
  container.innerHTML = "";
  const res = await fetch(API_URL);
  const itens = await res.json();

  itens.forEach((item) => {
    const card = document.createElement("div");
    card.className = "livro-card";
    card.classList.add(`tipo-${item.tipo}`);
    card.innerHTML = `
      <h3>${item.titulo}</h3>
      <p><strong>${item.tipo}</strong> por ${item.autor}</p>
      <div class="card-actions">
        <button onclick="editarItem(${item.id}, '${item.titulo}', '${item.autor}', '${item.tipo}')">Editar</button>
        <button onclick="deletarItem(${item.id})">Excluir</button>
      </div>
    `;
    container.appendChild(card);
  });
}

function editarItem(id, tituloAtual, autorAtual, tipoAtual) {
  Swal.fire({
    title: 'Editar Item',
    html: `
      <input id="editTitulo" class="swal2-input" value="${tituloAtual}" placeholder="Título">
      <input id="editAutor" class="swal2-input" value="${autorAtual}" placeholder="Autor">
      <select id="editTipo" class="swal2-input">
        <option value="livro" ${tipoAtual === "livro" ? "selected" : ""}>Livro</option>
        <option value="revista" ${tipoAtual === "revista" ? "selected" : ""}>Revista</option>
        <option value="publicacao" ${tipoAtual === "publicacao" ? "selected" : ""}>Publicação</option>
      </select>
    `,
    showCancelButton: true,
    confirmButtonText: 'Salvar',
    preConfirm: () => {
      const titulo = document.getElementById("editTitulo").value;
      const autor = document.getElementById("editAutor").value;
      const tipo = document.getElementById("editTipo").value;
      return { titulo, autor, tipo };
    }
  }).then(async (result) => {
    if (result.isConfirmed) {
      const { titulo, autor, tipo } = result.value;
      await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, titulo, autor, tipo }),
      });
      Swal.fire("Atualizado!", "", "success");
      carregarItens();
    }
  });
}

async function deletarItem(id) {
  const confirm = await Swal.fire({
    title: 'Tem certeza?',
    text: "Essa ação não pode ser desfeita.",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#e03131',
    cancelButtonColor: '#aaa',
    confirmButtonText: 'Sim, deletar!'
  });

  if (confirm.isConfirmed) {
    await fetch(`${API_URL}/${id}`, {
      method: "DELETE",
    });
    Swal.fire('Removido!', '', 'success');
    carregarItens();
  }
}

carregarItens();
