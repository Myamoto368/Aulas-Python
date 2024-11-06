import streamlit as st
from PIL import Image

# Configurações iniciais da página com tema preto e roxo
st.set_page_config(page_title="Portfólio e Currículo", layout="wide")
st.markdown("""
    <style>
        .reportview-container {
            background-color: #111111;
        }
        .sidebar .sidebar-content {
            background-color: #2e003e;
            color: white;
        }
        .sidebar .sidebar-content a {
            color: white;
        }
        .css-1d391kg {
            background-color: #111111;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Foto do desenvolvedor
foto = Image.open("foto_desenvolvedor.jpg")  # Substitua com o caminho da sua foto
st.sidebar.image(foto, width=150)

# Informações pessoais abaixo da foto
st.sidebar.write("**Nome:** Vitor Cardoso da Silva Lopes")
st.sidebar.write("**Profissão:** Desenvolvedor Full Stack")
st.sidebar.write("**Localização:** São Paulo, Brasil")

# Menu de navegação lateral
st.sidebar.title("Navegação")
secoes = [
    "Resumo das Qualificações",
    "Experiência Profissional",
    "Educação",
    "Habilidades Técnicas",
    "Projetos e Realizações",
    "Idiomas",
    "Cursos e Treinamentos",
    "Referências Profissionais",
    "Contato",
    "Portfólio de Projetos"
]
escolha = st.sidebar.radio("Selecione uma seção:", secoes)

# Função para mostrar o conteúdo de cada seção
def mostrar_secao(secao):
    if secao == "Resumo das Qualificações":
        st.header("Resumo das Qualificações")
        st.write("""
        Desenvolvedor Full Stack com mais de 8 anos de experiência no desenvolvimento de aplicações web e móveis.
        Sólidos conhecimentos em linguagens de programação como Python, JavaScript, C, Ruby, PHP, e frameworks como Django e React.
        Habilidade em trabalhar de forma colaborativa com equipes de desenvolvimento, design e produto para entregar soluções de alta qualidade.
        Focado na criação de aplicações escaláveis, seguras e de fácil manutenção.
        """)

    elif secao == "Experiência Profissional":
        st.header("Experiência Profissional")
        st.write("""
        **Tech Solutions Inc.**  
        *Desenvolvedor Full Stack*  
        Janeiro de 2018 - Presente  
        - Liderou o desenvolvimento de uma plataforma de e-commerce, resultando em um aumento de 30% nas vendas da empresa.
        - Implementou integrações com APIs de terceiros, como pagamento e envio, melhorando a experiência do usuário.
        - Trabalhou em estreita colaboração com o time de UX/UI para aprimorar a interface e usabilidade da plataforma.
        - Utilizou práticas de desenvolvimento ágil, participando de sprints e colaborando ativamente com as equipes.

        **StartUp Labs**  
        *Desenvolvedor Back-End*  
        Maio de 2015 - Dezembro de 2017  
        - Desenvolveu e manteve APIs RESTful para aplicativos móveis e web.
        - Implementou soluções de segurança de dados para proteger as informações dos usuários.
        - Automatizou processos internos, reduzindo o tempo de resposta em 20%.
        """)

    elif secao == "Educação":
        st.header("Educação")
        st.write("""
        **Universidade Federal de Tecnologia**  
        *Bacharelado em Ciência da Computação*  
        2011 - 2015  

        **Curso Técnico em Informática**  
        *Escola Técnica Profissionalizante*  
        2009 - 2011
        """)

    elif secao == "Habilidades Técnicas":
        st.header("Habilidades Técnicas")
        st.write("- Linguagens de Programação: Python, JavaScript, SQL")
        st.write("- Frameworks: Django, Flask, React, Node.js")
        st.write("- Ferramentas: Docker, Git, Jenkins, AWS, Firebase")
        st.write("- Metodologias: Desenvolvimento Ágil (Scrum, Kanban), TDD, CI/CD")

    elif secao == "Projetos e Realizações":
        st.header("Projetos e Realizações")
        st.write("Projeto 1: **Plataforma de Gerenciamento de Tarefas**")
        st.write("""
        - Desenvolveu uma aplicação de gerenciamento de tarefas com funcionalidades de colaboração em tempo real.
        - Utilizou tecnologias como React para o front-end e Django para o back-end.
        - A plataforma atraiu mais de 10.000 usuários ativos nos primeiros seis meses.
        """)

        st.write("Projeto 2: **Sistema de Recomendação de Produtos para E-commerce**")
        st.write("""
        - Criou um sistema de recomendação que aumentou a taxa de conversão de produtos em 15%.
        - Implementou algoritmos de machine learning para prever as preferências dos usuários.
        - Utilizou AWS para o processamento e armazenamento de dados, melhorando a escalabilidade.
        """)

    elif secao == "Idiomas":
        st.header("Idiomas")
        st.write("- Português: Nativo")
        st.write("- Inglês: Avançado (TOEFL: 100)")
        st.write("- Espanhol: Intermediário")

    elif secao == "Cursos e Treinamentos":
        st.header("Cursos e Treinamentos")
        st.write("**Curso de Machine Learning com Python** - Udacity (2020)")
        st.write("**Certificação em Desenvolvimento Web Full Stack** - Coursera (2019)")
        st.write("**Workshop de DevOps e CI/CD** - Alura (2018)")

    elif secao == "Referências Profissionais":
        st.header("Referências Profissionais")
        st.write("Nome: João Silva")
        st.write("Empresa: Tech Solutions Inc.")
        st.write("Cargo: Gerente de Projetos")
        st.write("Contato: joao.silva@techsolutions.com")

        st.write("Nome: Maria Oliveira")
        st.write("Empresa: StartUp Labs")
        st.write("Cargo: Líder de Tecnologia")
        st.write("Contato: maria.oliveira@startuplabs.com")

    elif secao == "Contato":
        st.header("Contato")
        st.write("Email: desenvolvedor@exemplo.com")
        st.write("LinkedIn: [linkedin.com/in/desenvolvedor](https://linkedin.com/in/desenvolvedor)")
        st.write("GitHub: [github.com/desenvolvedor](https://github.com/Myamoto368/")
        st.write("Site: [www.desenvolvedor.com](https://www.desenvolvedor.com)")

    elif secao == "Portfólio de Projetos":
        st.header("Portfólio de Projetos")
        st.write("Aqui estão alguns dos meus projetos recentes:")

        st.subheader("Projeto 1: Aplicação de Gerenciamento de Tarefas")
        st.write("""
        Descrição: Uma aplicação que permite aos usuários gerenciar suas tarefas diárias de forma colaborativa.
        - Tecnologias: Python, Django, React
        - GitHub: [Link para o repositório](https://github.com/Myamoto368/)
        """)

        st.subheader("Projeto 2: Site de E-commerce")
        st.write("""
        Descrição: Plataforma completa de e-commerce com sistema de recomendação de produtos.
        - Tecnologias: Node.js, React, MongoDB
        - GitHub: [Link para o repositório](https://github.com/exemplo/projeto2)
        """)

        st.subheader("Projeto 3: Sistema de Automação de Relatórios")
        st.write("""
        Descrição: Sistema para geração automática de relatórios semanais e mensais para equipes de vendas.
        - Tecnologias: Flask, SQLAlchemy, Pandas
        - GitHub: [Link para o repositório](https://github.com/exemplo/projeto3)
        """)

# Exibir a seção selecionada
mostrar_secao(escolha)
