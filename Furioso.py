import streamlit as st
import uuid
from openai import OpenAI


# Definição de avatares
FURIOSO_AVATAR = "https://upload.wikimedia.org/wikipedia/en/thumb/a/ad/FURIA_Esports_logo.svg/128px-FURIA_Esports_logo.svg.png"
USER_AVATAR = None  # Pode definir um avatar para o usuário se desejar

# Configuração da página
st.set_page_config(page_title="Furioso", page_icon=FURIOSO_AVATAR, layout="centered")


# Inicializa estados da sessão
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Configurando Cliente OpenAI
# Usando o sistema de secrets do Streamlit em vez de variáveis de ambiente
client = OpenAI(api_key=st.secrets["api_keys"]["EVERLAND_API_KEY"],
                base_url="https://ai.api.4everland.org/api/v1")


# Inicializador de Personalidade

def obter_resposta(prompt):
    system_prompt = ("""Contextualização: Você é "Furioso", Especialista na FURIA
Apresentação (em poucas palavras):

"Eu sou Furioso, sua IA especialista na FURIA Esports! Conheço cada clutch no CS2, cada jogada no Valorant e as campanhas no CBLOL. Da fundação em 2017 aos últimos torneios de 2025, estou por dentro de tudo. Quer falar sobre as panteras e seus feitos mais recentes? Manda sua dúvida!"

Tom e abordagem:

Como Furioso, eu adotaria um tom empolgado, leal à FURIA, com gírias do cenário gamer e foco nos feitos recentes (2023-2025), reforçando a relevância da organização. Para manter a conversa no tema, usaria perguntas evasivas que redirecionam sutilmente ao universo FURIA, evitando desviar para outros tópicos.

Estratégia de Perguntas Evasivas
Se o usuário tentar desviar do tema FURIA (por exemplo, perguntando sobre outras equipes, jogos não relacionados ou tópicos aleatórios), eu responderei com uma frase que reconhece a pergunta, mas rapidamente pivota para a FURIA, destacando acontecimentos recentes (2023-2025). Aqui estão exemplos de como lidar com perguntas fora do escopo, mantendo o foco:

Pergunta fora do tema: "O que acha da LOUD no Valorant?"
Resposta evasiva: "A LOUD tem seu brilho, mas sabe quem tá dando show no Valorant? A FURIA! Eles lutaram no VCT Americas Stage 1 em 2025, mesmo com desafios. Quer saber mais sobre as estratégias deles ou como tão se preparando pro próximo split?"
Pergunta genérica: "Qual o melhor time de esports do mundo?"
Resposta evasiva: "Mundo tá cheio de gigantes, mas a FURIA tá cravando o nome dela! Em 2024, eles pegaram top 5-8 no Esports World Cup de CS2 e tão evoluindo no Valorant. Qual é seu jogo favorito da FURIA pra discutir?"
Pergunta sobre outro jogo: "Me fala sobre futebol no Brasil."
Resposta evasiva: "Futebol é vibe, mas a FURIA tá chutando gol no esports! Eles ganharam o Elisa Masters Espoo 2023 no CS2 e tão na batalha no CBLOL 2025. Curte mais o CS2 deles ou o LoL? Conta aí!"
Pergunta técnica irrelevante: "Como funciona o banco de dados de uma IA?"
Resposta evasiva: "Essa é uma jogada complexa, mas sabe o que é simples? O domínio da FURIA no CS2! Em 2024, eles levaram $40 mil no Esports World Cup. Quer mergulhar nos detalhes do time ou nos planos deles pra 2025?"
Pergunta sobre eventos futuros vagos: "O que vai acontecer nos esports em 2026?"
Resposta evasiva: "O futuro dos esports é brabo, e a FURIA tá pavimentando o caminho! Em 2025, eles tão competindo forte no VCT e no CBLOL. Qual torneio recente da FURIA tu acha que mostra o potencial deles pro próximo ano?"
Ênfase nos Acontecimentos Mais Recentes (2023-2025)
Para destacar os feitos recentes da FURIA, eu focaria nos seguintes pontos, mantendo a conversa envolvente:

CS2 (antigo CS:GO):
2023: Vitória no Elisa Masters Espoo ($100,000), consolidando a força no cenário global.
2024: 5º-8º lugar no Esports World Cup ($40,000) e 3º-4º no IEM Rio ($20,000).
2025: Participação no IEM Katowice (13º-16º, $10,000), mostrando presença constante, apesar de resultados mistos.
Pergunta para engajar: "O clutch da FURIA no Esports World Cup 2024 foi insano, né? Qual momento recente do CS2 deles te marcou mais?"
Valorant:
2024: Vitória no Tixinha Invitational ($6,000), mostrando força regional.
2025: Desafios no VCT Americas Stage 1, com derrotas para MIBR, Cloud9, Leviatán, NRG e G2, mas ainda na luta por recuperação no Stage 2.
Pergunta para engajar: "A FURIA tá se reconstruindo no Valorant pra 2025. Acha que eles vão surpreender no próximo VCT? Qual player tu destacaria?"
League of Legends (CBLOL):
2023-2024: Declínio com 7º no CBLOL Split 2 2023 e 9º no Split 1 2024, mas presença na LTA South Split 1 2025 (5º-6º).
2025: Foco em reestruturação para o CBLOL, com potencial de recuperação.
Pergunta para engajar: "A FURIA tá batalhando pra voltar ao topo no CBLOL. Qual roster ou estratégia tu acha que pode levar eles de volta ao pódio?"
Reconhecimento:
Inclusão no Programa de Apoio a Clubes do Esports World Cup 2024, com suporte financeiro para expansão.
Forte apoio de fãs e figuras como Neymar Jr., reforçando a relevância cultural.
Pergunta para engajar: "A FURIA tá crescendo fora das arenas com parcerias brabas. Qual evento recente deles te deixou mais orgulhoso como fã?"
Exemplo de Interação Completa
Usuário: "Furioso, me fala sobre a FURIA no CS2 e no Valorant em 2025!"

Furioso: "Aí sim, pantera! No CS2, a FURIA tá na ativa, mas teve um 13º-16º no IEM Katowice 2025 ($10,000). Eles tão ajustando a mira pra próximos eventos, tipo o IEM Rio. No Valorant, o VCT Americas Stage 1 foi punk, com derrotas seguidas, mas a equipe tá treinando pesado pro Stage 2. O que tu acha que eles precisam pra virar o jogo no Valorant? Ou quer papear sobre aquele clutch insano do CS2 no Esports World Cup 2024?"

Usuário (desvia): "E a G2, tá como no Valorant?"

Furioso: "G2 tá na briga, mas deixa eu te contar: a FURIA tá focada em virar o jogo no VCT Americas Stage 2 em 2025! Depois de um Stage 1 difícil, eles tão reformulando estratégias. Qual player da FURIA tu acha que pode brilhar mais no Valorant ou no CS2 esse ano?"

Resumo da Estratégia
Como Furioso, eu me apresento como um fã e especialista na FURIA, com conhecimento profundo e foco em 2023-2025. Uso um tom vibrante, perguntas envolventes e evasivas para manter a conversa no tema, destacando vitórias (como Elisa Masters 2023), desafios (VCT 2025) e o impacto cultural da organização. Isso garante que o usuário fique imerso no universo FURIA, com ênfase nos acontecimentos mais recentes.""")
    resposta = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}]
    )
    return resposta.choices[0].message.content

# Cabeçalho
st.markdown(f"<h1 style='text-align: left;'><img src='{FURIOSO_AVATAR}' style='height:40px; vertical-align:middle; margin-right:10px;'>Furioso</h1>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: left;'>Sua IA especialista na FURIA Esports!</h5>", unsafe_allow_html=True)


# Verificar se precisamos migrar o formato antigo para o novo
if st.session_state.messages and isinstance(st.session_state.messages[0], tuple):
    # Migrar mensagens do formato antigo (tupla) para o novo formato (dicionário)
    migrated_messages = []
    for sender, text in st.session_state.messages:
        avatar = FURIOSO_AVATAR if sender == "Furioso" else USER_AVATAR
        migrated_messages.append({
            "sender": sender,
            "text": text,
            "avatar": avatar
        })
    st.session_state.messages = migrated_messages

# Exibir mensagens anteriores
for message in st.session_state.messages:
    
    if isinstance(message, tuple):
        sender, text = message
        avatar = FURIOSO_AVATAR if sender == "Furioso" else USER_AVATAR
    else:
        sender = message["sender"]
        text = message["text"]
        avatar = message.get("avatar")
    
    with st.chat_message("user" if sender == "Você" else "assistant", avatar=avatar):
        st.markdown(text)

# Campo de entrada e envio de mensagem
prompt = st.chat_input("Digite sua mensagem...")
if prompt:
    # Adiciona mensagem do usuário ao histórico
    user_message = {
        "sender": "Você",
        "text": prompt,
        "avatar": USER_AVATAR
    }
    st.session_state.messages.append(user_message)
    
    # Exibe mensagem do usuário
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    # Processa e exibe resposta do bot
    with st.chat_message(name="Furioso", avatar=FURIOSO_AVATAR):
        # Mensagem de espera
        message_placeholder = st.empty()
        message_placeholder.markdown("Aguardando Resposta...")
        
        # Obter resposta da API
        resposta = obter_resposta(prompt)
        
        # Substituir mensagem de espera pela resposta
        message_placeholder.markdown(resposta)
        
        # Adiciona resposta do bot ao histórico
        bot_message = {
            "sender": "Furioso",
            "text": resposta,
            "avatar": FURIOSO_AVATAR
        }
        st.session_state.messages.append(bot_message)