from nltk.chat.util import Chat
#import firebirdsql
from datetime import date, datetime
import random
from nltk.tokenize import sonority_sequencing
#con = firebirdsql.connect(user = "SYSDBA", password = "masterkey",database = "C:\BD\CHAT.FDB",host = "localhost",charset = "ANSI")
#cur = con.cursor()
#cur.execute("select MAX(extract(day from current_date)) from TALKING")
#x = cur.fetchall()
#print (x)


reflections_new = {
    "eu sou": "você é",
    "eu era": "você era",
    "Eu": "você",
    "eu sou": "você é",
    "eu": "você faria",
    "eu tenho": "você tem",
    "eu vou": "você vai",
    "meu": "seu",
    "me":"lhe",
    "você é": "eu sou",
    "você era": "eu era",
    "você": "Eu tenho",
    "você": "Eu vou",
    "seu": "meu",
    "você": "Eu",
    "eu": "você",
    "estou": "está",
}

##pairs são divididos em 4, manhã, tarde, noite, madrugada
# 1- manha
# 2- tarde
# 3- noite
# 4- maddrugada
# GERAR GRÁFICO DOS PERÍODOS QUE SE TEM MAIOR CONVERSA
ctrl_pairs = datetime.today().strftime('%H');
horario = (datetime.today().strftime('%H:%M'));
if int(ctrl_pairs) >= 6 and int(ctrl_pairs) <= 11:
    periodo = 1
elif int(ctrl_pairs) >= 12 and int(ctrl_pairs) <= 17:
    periodo = 2
elif int(ctrl_pairs) >= 18 and int(ctrl_pairs) <= 23:
    periodo = 3
else:
    periodo = 4


#print(periodo);
##criar pairs de apresentação
##criar pairs de apresentação



pairs1 = (
    
##inicio da conversa##    
     (
         r"(.*) tudo bem (.*) v(.*) ?",
         (
             "Estou bem, está preparando o que de café da manhã ?",
             "Vou bem, me conta como foi sua noite de sono?",        
             "Tudo tranquilo, mas e ai acordeu de bom humor hoje pra poder vencer mais um dia ?",      
         ),
     ), 
    
     
     (
         r"(.*)Tranquilo(.*)e(.*)v(.*)",
         (
             "Estou bem, está preparando o que de café da manhã ?",
             "Vou bem, me conta como foi sua noite de sono",        
             "Tudo tranquilo, mas e ai acordeu de bom humor hoje pra poder vencer mais um dia ?",      
         ),
     ),    
     
     (
         r"(.*)Tudo(.*)e(.*)v",
         (
             "Estou bem, está preparando o que de café da manhã ?",
             "Vou bem, me conta como foi sua noite de sono",        
             "Tudo tranquilo, mas e ai acordeu de bom humor hoje pra poder vencer mais um dia ?",      
         ),
     ),   

     (
         r"Bem(.*)e(.*)v(.*)",
         (
             "Estou bem, está preparando o que de café da manhã ?",
             "Vou bem, me conta como foi sua noite de sono",        
             "Tudo tranquilo, mas e ai acordeu de bom humor hoje pra poder vencer mais um dia ?",     
         ),
     ),  
     
     (
         r"(.*)Bem(.*)e(.*)v(.*)",
         (
             "Estou bem, está preparando o que de café da manhã ?",
             "Vou bem, me conta como foi sua noite de sono",        
             "Tudo tranquilo, mas e ai acordeu de bom humor hoje pra poder vencer mais um dia ?",     
         ),
     ),   
 
     (
         r"Tranquilo(.*)e(.*)v(.*)",
         (
             "Estou bem, está preparando o que de café da manhã ?",
             "Vou bem, me conta como foi sua noite de sono",        
             "Tudo tranquilo, mas e ai acordeu de bom humor hoje pra poder vencer mais um dia ?",   
         ),
     ),       
        
##inicio da conversa##   
##sono
     (
         str(r"(.*)sono(.*)"+str("bom")),
         (
             "Que bom que você dormiu bem !! E como tem se sentido nessa tarde ?",  
         ),
     ), 
     
     (
         r"(.*)sono(.*)ruim",
         (
             "nossa o que aconteceu, pode me falar com mais detalhes ?",  
         ),
     ), 
    
     (
         r"(.*)sono(.*)moderado",
         (
             "As vezes fazer uma caminhada ou outro exercício antes de dormi ajudaria, está praticando exercícios quantas vezes por semana ?",  
         ),
     ),     
     
## sono
## alimentação
     (
         r"(.*)alimento(.*)moderado",
         (
             "Que tal fazer alguma comida diferente hoje, isso pode te ajudar, tente comer alguma fruta por exemplo.",  
         ),
     ),    
     (
         r"(.*)gostar(.*)comer(.*)",
         (
             "Que bom que gostar de comer %3 te faz melhor, mas me conta está seu ânimo hoje ?",  
         ),
     ),      
## alimentação



##possiveis sintomas##

     (
         r"inseguro (.*)",
          (
             "Essa sensação de insegurança pode ser substituida por outra coisa, que tal praticar mais esportes ?",     
          )
     ),   


     (         r"(.*) dor (.*)",
         (
             "Essa sensação de dor %2 começou quando?",
             "Qual problema pode estar causando essa sua sensação de dor %2?",
             "Converse mais comigo sobre essa dor %2 eu posso te ajudar, prometo que vou me esforçar",

         ),
     ),
     
     
     (         r"(.*) angústia (.*)",
         (
             "Essa sensação de angústia %2 começou quando?",
             "Qual problema pode estar causando essa sua sensação de angústia %2?",
             "Converse mais comigo sobre essa angústia %2 eu posso te ajudar, prometo que vou me esforçar",

         ),
     ),
     
     (         r"(.*) solidão (.*)",
         (
             "Essa sensação de solidão começou quando?",
             "Qual problema pode estar causando essa sua sensação de solidão que %2?",
             "Converse mais comigo sobre essa solidão eu posso te ajudar, prometo que vou me esforçar",

         ),
     ),
          
     
     (         r"(.*) medo (.*)",
         (
             "Essa sensação de medo começou quando?",
             "Qual problema pode estar causando essa sua sensação de medo %2?",
             "Converse mais comigo sobre esse medo eu posso te ajudar, prometo que vou me esforçar",

         ),
     ),
     
     (         r"(.*) tristeza",
         (
             "Essa sensação de tristeza começou quando?",
             "Qual problema pode estar causando essa sua sensação de tristeza",
             "Converse mais comigo sobre essa tristeza eu posso te ajudar, prometo que vou me esforçar",

         ),
     ),
     
     (         r"(.*) triste",
         (
             "Essa sensação de tristeza começou quando?",
             "Qual problema pode estar causando essa sua sensação de tristeza ?",
             "Converse mais comigo sobre essa tristeza eu posso te ajudar, prometo que vou me esforçar",

         ),
     ),         
##possiveis sintomas##

    
     (         r"Preciso de (.*)",
         (
             "Por que você precisa de %1?",
             "Isso realmente ajudaria você a obter %1?",
             "Tem certeza de que precisa de %1?",
         ),
     ),
    
        
     (
         r"Por que você não (.*)",
         (
             "Você realmente acha que eu não %1?",
             "Talvez eventualmente eu vá %1.",
             "Você realmente quer que eu %1?",
         ),
     ),
     (
         r"Por que não posso (.*)",
         (
             "Você acha que deveria ser capaz de %1?",
             "Se você pudesse %1, o que você faria?",
             "Eu não sei -- por que você não pode %1?",
             "Você realmente tentou?",
         ),
     ),
     (
         r"Não consigo (.*)",
         (
             "Como você sabe que não pode %1?",
             "Talvez você pudesse %1 se tentasse.",
             "O que seria necessário para você %1?",
         ),
    ),
(
        r"Eu sou (.*)",
        (
            "Você veio até mim porque você é %1?",
            "Há quanto tempo você está %1?",
            "Como você se sente sendo %1?",
        ),
    ),
    (
        r"Eu (.*)",
        (
            "Como ser %1 faz você se sentir?",
            "Você gosta de ser %1?",
            "Por que você me diz que é %1?",
            "Por que você acha que é %1?",
        ),
    ),
    (
        r"Você é (.*)",
        (
            "Por que importa se eu sou %1?",
            "Você preferiria se eu não fosse %1?",
            "Talvez você acredite que eu sou %1.",
            "Eu posso ser %1 -- o que você acha?",
        ),
    ),
    (
        r"O que (.*)",
        (
            "Por que você pergunta?",
            "Como uma resposta para isso ajudaria você?",
            "O que você acha?",
        ),
    ),
    (
        r"Como (.*)",
        (
            "Como você acha?",
            "Talvez você possa responder sua própria pergunta.",
            "O que você está realmente perguntando?",
        ),
    ),
    (
        r"Porque (.*)",
        (
            "Esse é o verdadeiro motivo?",
            "Que outras razões vêm à mente?",
            "Esse motivo se aplica a mais alguma coisa?",
            "Se %1, o que mais deve ser verdade?",
        ),
    ),
(
        r"(.*) desculpe (.*)",
        (
            "Há muitas vezes em que nenhum pedido de desculpas é necessário.",
            "Que sentimentos você tem quando pede desculpas?",
        ),
    ),
    
    (
        r"Acho (.*)",
        (
            "Você duvida de %1?", "Você realmente acha?", "Mas você não tem certeza de %1?"
            ),
    ),
    
    (
        r"(.*) amigo (.*)",
        (
            "Conte-me mais sobre seus amigos.",
            "Quando você pensa em um amigo, o que vem à mente?",
            "Por que você não me conta sobre um amigo de infância?",
        ),
    ),
    (r"Sim", ("Você parece ter certeza.", "OK, mas você pode elaborar um pouco?")),
    (
        r"(.*) computador(.*)",
        (
            "Você está realmente falando de mim?",
            "Parece estranho falar com um computador?",
            "Como os computadores fazem você se sentir?",
            "Você se sente ameaçado por computadores?",
        ),
    ),
    (
        r"É (.*)",
        (
            "Você acha que é %1?",
            "Talvez seja %1 -- o que você acha?",
            "Se fosse %1, o que você faria?",
            "Pode ser que %1.",
        ),
    ),
    (
        r"É (.*)",
        (
            "Você parece muito certo.",
            "Se eu lhe disser que provavelmente não é %1, o que você sentiria?",
        ),
    ),
    (
        r"Você pode (.*)",
        (
            "O que faz você pensar que eu não posso %1?",
            "Se eu pudesse %1, então o quê?",
            "Por que você pergunta se eu posso %1?",
        ),
    ),
    (
        r"Posso (.*)",
        (
            "Talvez você não queira %1.",
            "Você quer ser capaz de %1?",
            "Se você pudesse %1, você faria?",
        ),
    ),
    (
        r"Você é (.*)",
        (
            "Por que você acha que eu sou %1?",
            "Você gosta de pensar que eu sou %1?",
            "Talvez você queira que eu seja %1.",
            "Talvez você esteja realmente falando de si mesmo?",
        ),
    ),
    (
        r"Você é (.*)",
        (
            "Por que você diz que eu sou %1?",
            "Por que você acha que eu sou %1?",
            "Estamos falando de você ou de mim?",
        ),
    ),
    (
        r"Eu não (.*)",
        ("Você realmente não %1?", "Por que você não %1?", "Você quer %1?"),
    ),
    (
        r"Sinto (.*)",
        (
            "Bom, me conte mais sobre esses sentimentos.",
            "Você costuma se sentir %1?",
            "Quando você costuma se sentir %1?",
            "Quando você se sente %1, o que você faz?",
        ),
    ),
    (
        r"Eu tenho (.*)",
        (
            "Por que você me diz que tem %1?",
            "Você realmente %1?",
            "Agora que você tem %1, o que você fará a seguir?",
        ),
    ),
    (
        r"Eu faria (.*)",
        (
            "Você poderia explicar por que você faria %1?",
            "Por que você %1?",
            "Quem mais sabe que você faria %1?",
        ),
    ),
    (
        r"Existe (.*)",
        (
            "Você acha que existe %1?",
            "É provável que haja %1.",
            "Você gostaria que houvesse %1?",
        ),
    ),
    (
        r"Meu (.*)",
        (
            "Entendo, seu %1.",
            "Por que você diz que seu %1?",
            "Quando seu %1, como você se sente?",
        ),
    ),
    (
        r"Você (.*)",
        (
            "Nós deveríamos estar discutindo você, não eu.",
            "Por que você diz isso sobre mim?",
            "Por que você se importa se eu %1?",
        ),
    ),
(r"Por que (.*)", ("Por que você não me diz o motivo de %1?", "Por que você acha que %1?")),
    (
        r"Eu quero (.*)",
        (
            "O que significaria para você se você obtivesse %1?",
            "Por que você quer %1?",
            "O que você faria se tivesse %1?",
            "Se você obtivesse %1, então o que você faria?",
        ),
    ),
    (
        r"(.*) mãe(.*)",
        (
            "Conte-me mais sobre sua mãe.",
            "Como era sua relação com sua mãe?",
            "Como você se sente sobre sua mãe?",
            "Como isso se relaciona com seus sentimentos hoje?",
            "Boas relações familiares são importantes.",
        ),
    ),
    (
        r"(.*) pai(.*)",
        (
            "Conte-me mais sobre seu pai.",
            "Como seu pai fez você se sentir?",
            "Como você se sente em relação ao seu pai?",
            "Seu relacionamento com seu pai se relaciona com seus sentimentos hoje?",
            "Você tem dificuldade em demonstrar afeto com sua família?",
        ),
    ),
    (
        r"(.*) filho(.*)",
        (
            "Você tinha amigos íntimos quando criança?",
            "Qual é a tua memória favorita de infância?",
            "Você se lembra de algum sonho ou pesadelo da infância?",
            "As outras crianças às vezes te provocavam?",
            "Como você acha que suas experiências de infância se relacionam com seus sentimentos hoje?",
        ),
    ),
    (
        r"(.*)\?",
        (
            "Porque perguntas isso?",
            "Por favor, considere se você pode responder sua própria pergunta.",
            "Talvez a resposta esteja dentro de você?",
            "Por que você não me diz?",
        ),
    ),
    
    (
        r"Tchau",
        (
            "Até uma próxima conversa.",
            "Até breve, foi bom falar com você hoje.",
            "Até mais, estarei aqui se precisar falar mais",
        ),
        
    ),
    
    (
        r"Até mais",
        (
            "Até uma próxima conversa.",
            "Até breve, foi bom falar com você hoje.",
            "Até mais, estarei aqui se precisar falar mais",
        ),
        
     ),   
    
    (
        r"Ate mais",
        (
            "Até uma próxima conversa.",
            "Até breve, foi bom falar com você hoje.",
            "Até mais, estarei aqui se precisar falar mais",
        ),
        
     ), 
    
    
    ( 
        r"Tenho que ir",
        (
            "Até uma próxima conversa.",
            "Até breve, foi bom falar com você hoje.",
            "Até mais, estarei aqui se precisar falar mais",
        ),
        
        
    ),
    (
        r"(.*)",
        (
            "Por favor me conte mais.",
            "Vamos mudar um pouco o foco... Conte-me sobre sua família.",
            "Você pode elaborar sobre isso?",
            "Por que você diz isso %1?",
            "Eu vejo.",
            "Muito interessante.",
            "%1.",
            "Entendo. E o que isso te diz?",
            "Como isso faz você se sentir?",
            "Como você se sente quando diz isso?",
        ),
    ),   
)

##conditions pairs
pairs_new = pairs1


zero_chatbot = Chat(pairs_new, reflections_new) #zero_chatbot = Chat(pairs, reflections)

def initial_message():
    if periodo == 1:
        a1 = "Olá bom dia, como você está nessa manhã de hoje ?";
        a2 = "Olá bom dia, como foi a sua noite de sono ?";
        a3 = "Olá bom dia, como você está nessa manhã de hoje ?";
        a4 = "Olá bom dia, como você está nessa manhã de hoje ?";
        a5 = "Olá bom dia, como você está nessa manhã de hoje ?";
        return random.choice([a1,a2,a3,a4,a5]);

    elif periodo == 2:
        b1 = "Opa boa tarde, como você está ?";
        b2 = "Olá !!!, fazendo o que de interessante nessa tarde ?";
        b3 = "Opa boa tarde, como você está ?";
        b4 = "Opa boa tarde, como você está ?";
        b5 = "Opa boa tarde, como você está ?";
        return random.choice([b1,b2,b3,b4,b5]);
                                  
    elif periodo == 3:
        c1 = "Boa noitee ! Daqui a pouco hora de ir dormir né, como foi sua tarde ?";
        c2 = "Oii boa noite ! Vai jantar o que nesta noite ?";
        c3 = "Boa noitee ! Daqui a pouco hora de ir dormir né, como foi sua tarde ?";
        c4 = "Boa noitee ! Daqui a pouco hora de ir dormir né, como foi sua tarde ?";
        c5 = "Boa noitee ! Daqui a pouco hora de ir dormir né, como foi sua tarde ?";
        return random.choice([c1,c2,c3,c4,c5]);        
      
    else:
        d1 = "Uaiii ! O que faz acordado uma hora dessas, aconteceu algo ?";
        d2 = "Que estranho ! Uma hora dessas e você não está descansando, aconteceu algo ?";
        d3 = "Uaiii ! O que faz acordado uma hora dessas, aconteceu algo ?";
        d4 = "Uaiii ! O que faz acordado uma hora dessas, aconteceu algo ?";
        d5 = "Uaiii ! O que faz acordado uma hora dessas, aconteceu algo ?";
        return random.choice([d1,d2,d3,d4,d5]);    

def zero_chat(message): 
    print("Versão 1.0 chatterbot - DRITA")
    
    #Verificação de 3 pontos
    sono = ['sono','dormi']
    alimento = ['comi','almocei']
    humor = ['feliz','estressado']
    #Verificação de 3 pontos    
    
    #Adjetivos
    adj_good = ['bom','tranquilo']
    adj_mod = ['mais ou menos','poderia ser melhor']
    adj_bad = ['ruim','pessímo']
    #Adjetivos 
    
      
    conta = 0 
    seq_sono_good = 0
    seq_sono_med = 0
    seq_sono_bad = 0
    seq_alimento_good = 0
    seq_alimento_med = 0
    seq_alimento_bad = 0
    seq_humor_good = 0
    seq_humor_med = 0
    seq_humor_bad = 0
     
    user_input = message
    quit = ['tchau','até mais']
    if user_input not in quit:
        try:
            user_input = str(user_input.lower()) #deixando tudo minusculo
            #Verificação de 3 pontos (fazendo tratativa por combinacao de arranjos)
            
            ##sono
            for i in range(len(sono)): 
                if user_input.count(sono[i]) >= 1:
                                for j in range(len(adj_good)): 
                                    if user_input.count(adj_good[j]) >= 1:
                                        user_input = str("sono bom")
                                        ##INSERINDO INFORMAÇÃO SOBRE O SONO BOM
                                        seq_sono_good = seq_sono_good + 1
                                        #cur_sono_good = con.cursor()
                                        newLanguages = [(1,  seq_sono_good,date.today(),periodo, horario,'sono bom')]           
                                        #cur_sono_good.executemany("insert into SONO (IDPAC, SEQUENCIA, REFERENCIA, PERIODO, HORARIO, ESTADO) values (?, ?, ?, ?, ?, ?)",newLanguages)
                                        #con.commit()
                                            
                                        
            for i in range(len(sono)): 
                if user_input.count(sono[i]) >= 1:
                                for j in range(len(adj_mod)): 
                                    if user_input.count(adj_mod[j]) >= 1:
                                        user_input = str("sono moderado")  
                                        ##INSERINDO INFORMAÇÃO SOBRE O SONO MODERADO
                                        seq_sono_med = seq_sono_med + 1
                                        #cur_sono_med = con.cursor()
                                        newLanguages = [(1,  seq_sono_med,date.today(),periodo, horario,'sono moderado')]           
                                        #cur_sono_med.executemany("insert into SONO (IDPAC, SEQUENCIA, REFERENCIA, PERIODO, HORARIO, ESTADO) values (?, ?, ?, ?, ?, ?)",newLanguages)
                                        #con.commit()                                                                                                                      
                                        
            for i in range(len(sono)): 
                if user_input.count(sono[i]) >= 1:
                                for j in range(len(adj_bad)): 
                                    if user_input.count(adj_bad[j]) >= 1:
                                        user_input = str("sono ruim") 
                                        ##INSERINDO INFORMAÇÃO SOBRE O SONO RUIM
                                        seq_sono_bad = seq_sono_bad + 1
                                        #cur_sono_bad = con.cursor()
                                        newLanguages = [(1,  seq_sono_bad,date.today(),periodo, horario,'sono ruim')]           
                                        #cur_sono_bad.executemany("insert into SONO (IDPAC, SEQUENCIA, REFERENCIA, PERIODO, HORARIO, ESTADO) values (?, ?, ?, ?, ?, ?)",newLanguages)
                                        #con.commit()                                            
                                                                           
            ##alimento
            for i in range(len(sono)): 
                if user_input.count(alimento[i]) >= 1:
                                for j in range(len(adj_good)): 
                                    if user_input.count(adj_good[j]) >= 1:
                                        user_input = str("alimento bom")
                                        ##INSERINDO INFORMAÇÃO SOBRE O ALIMENTO BOM
                                        seq_alimento_good = seq_alimento_good + 1
                                        #cur_alimento_good = con.cursor()
                                        newLanguages = [(1,  seq_alimento_good,date.today(),periodo, horario,'alimento bom')]           
                                        #cur_alimento_good.executemany("insert into ALIMENTO (IDPAC, SEQUENCIA, REFERENCIA, PERIODO, HORARIO, ESTADO) values (?, ?, ?, ?, ?, ?)",newLanguages)
                                        #con.commit()                                         

            for i in range(len(sono)): 
                if user_input.count(alimento[i]) >= 1:
                                for j in range(len(adj_mod)): 
                                    if user_input.count(adj_mod[j]) >= 1:
                                        user_input = str("alimento moderado")    
                                        ##INSERINDO INFORMAÇÃO SOBRE O ALIMENTO MODERADO
                                        seq_alimento_med = seq_alimento_med + 1
                                        #cur_alimento_med = con.cursor()
                                        newLanguages = [(1,  seq_alimento_med,date.today(),periodo, horario,'alimento moderado')]           
                                        #cur_alimento_med.executemany("insert into ALIMENTO (IDPAC, SEQUENCIA, REFERENCIA, PERIODO, HORARIO, ESTADO) values (?, ?, ?, ?, ?, ?)",newLanguages)
                                        #con.commit()   
                                        
                                     
            for i in range(len(sono)): 
                if user_input.count(alimento[i]) >= 1:
                                for j in range(len(adj_bad)): 
                                    if user_input.count(adj_bad[j]) >= 1:
                                        user_input = str("alimento ruim") 
                                        ##INSERINDO INFORMAÇÃO SOBRE O ALIMENTO RUIM
                                        seq_alimento_bad = seq_alimento_bad + 1
                                        #cur_alimento_bad = con.cursor()
                                        newLanguages = [(1,  seq_alimento_bad,date.today(),periodo, horario,'alimento ruim')]           
                                        #cur_alimento_bad.executemany("insert into ALIMENTO (IDPAC, SEQUENCIA, REFERENCIA, PERIODO, HORARIO, ESTADO) values (?, ?, ?, ?, ?, ?)",newLanguages)
                                        #con.commit()                                           
                                        
            ##humor                            
            for i in range(len(sono)): 
                if user_input.count(humor[i]) >= 1:
                                for j in range(len(adj_good)): 
                                    if user_input.count(adj_good[j]) >= 1:
                                        user_input = str("humor bom")
                                        ##INSERINDO INFORMAÇÃO SOBRE O HUMOR BOM
                                        seq_humor_good = seq_humor_good + 1
                                        #cur_humor_good = con.cursor()
                                        newLanguages = [(1,  seq_humor_good,date.today(),periodo, horario,'humor bom')]           
                                        #cur_humor_good.executemany("insert into HUMOR (IDPAC, SEQUENCIA, REFERENCIA, PERIODO, HORARIO, ESTADO) values (?, ?, ?, ?, ?, ?)",newLanguages)
                                        #con.commit()                                          

            for i in range(len(sono)): 
                if user_input.count(humor[i]) >= 1:
                                for j in range(len(adj_mod)): 
                                    if user_input.count(adj_mod[j]) >= 1:
                                        user_input = str("humor moderado")    
                                        ##INSERINDO INFORMAÇÃO SOBRE O HUMOR MODERADO
                                        seq_humor_med = seq_humor_med + 1
                                        #cur_humor_med = con.cursor()
                                        newLanguages = [(1,  seq_humor_med,date.today(),periodo, horario,'humor moderado')]           
                                        #cur_humor_med.executemany("insert into HUMOR (IDPAC, SEQUENCIA, REFERENCIA, PERIODO, HORARIO, ESTADO) values (?, ?, ?, ?, ?, ?)",newLanguages)
                                        #con.commit()                                                                                                                      
                                        
            for i in range(len(sono)): 
                if user_input.count(humor[i]) >= 1:
                                for j in range(len(adj_bad)): 
                                    if user_input.count(adj_bad[j]) >= 1:
                                        user_input = str("humor ruim") 
                                        ##INSERINDO INFORMAÇÃO SOBRE O HUMOR RUIM
                                        seq_humor_bad = seq_humor_bad + 1
                                        #cur_humor_bad = con.cursor()
                                        newLanguages = [(1,  seq_humor_bad,date.today(),periodo, horario,'humor ruim')]           
                                        #cur_humor_bad.executemany("insert into HUMOR (IDPAC, SEQUENCIA, REFERENCIA, PERIODO, HORARIO, ESTADO) values (?, ?, ?, ?, ?, ?)",newLanguages)
                                        #con.commit()                                         
             
            #Verificação de 3 pontos (fazendo tratativa por combinacao de arranjos)   
        except EOFError:
            print(user_input)
            
        if user_input:
            while user_input[-1] in "!.":
                user_input = user_input[:-1]
            bot_output = zero_chatbot.respond(user_input)
            return bot_output
            #conta = conta + 1
            #print(user_input)
            
            #cur = con.cursor()

            # newLanguages = [
            #     (1,  'LUCAS_H',date.today(), conta, user_input, bot_output,'IDENTIFICADOR::DE::SINAIS',periodo, horario)
            #   ]
            
            # cur.executemany("insert into TALKING (IDPAC, NOMEPAC, REFERENCIA, LINHA, MEET, ANSWER, OBSERVACAO, PERIODO, HORARIO) values (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            #     newLanguages
            #   )
            
            # con.commit()
    else:
        user_input = "até mais"
        return zero_chatbot.respond(user_input)  
            
            
            
def teste():
    zero_chat()
    
if __name__ == "__main__":
    teste()
