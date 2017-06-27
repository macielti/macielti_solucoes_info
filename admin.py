from datetime import datetime
import sys, os
print ("O que você deseja fazer? \n1.Adicionar um cliente. \n2. Adicionar atualização de serviço.")

option=input("")
############### Adição de um novo Client
if option == "1":
    os.system("clear")
    nome=input("Nome Completo do Cliente:\n")
    client_id=input("Digite o ID:\n")
    ### Pagina Html
    #Data
    now = datetime.now()
    year= str(now.year)
    month= str(now.month)
    day= str(now.day)
    #Gerando a pagina html
    name_archiv = "clients/"+client_id + ".html"
    arq = open(name_archiv, "a+")
    arq.writelines("""
        <html>\n
            <head>\n
                <!FAVICON>\n
                <link rel="icon" type="image/png" href="../imgs/image10.png">\n
                <title> """+ client_id +""" </title>\n
                <meta charset="UTF-8">\n
                <meta name="viewport" content="width=device-width, initial-scale=1.0">\n
                <!font awersome>\n
                <link href="../configs/font-awesome-4.7.0/css/font-awesome.min.css" rel="stylesheet" type="text/css"/>\n
                <!Bootstrap>\n
                <link href="../configs/bootstrap.min.css" rel="stylesheet" type="text/css"/>\n
                <!stylecss>\n
                <link href="../configs/style.css" rel="stylesheet" type="text/css"/>\n
                <meta name="robots" content="noindex">\n
            </head>\n
            <body class="body-comingsson">\n
                <script type="text/javascript" src="../configs/script.js"></script>\n
<!top da pagina>
        <div class="jumbotron text-center" id="jumbotrom-title">
            <h1 class="hvr-float-shadow">Maciel T.I - Soluções em Informática</h1>
            <p>Agende uma Visita e Conheça os Nossos Serviços. Porque os Seus Projetos Não Podem Ficar Parados</p> 
        </div>
    
        <!Menu grande>
        <div class="container-fluid fluid hidden-xs">
            <div class="row">
                <div class="col-md-4 col-md-offset-4">
                    <ul class="menutitulo">
                        <a href="#"><li class="h3 hvr-underline-from-left">Inicio</li></a>

                        <a href="#pe"><li class="h3 hvr-underline-from-left">Contato</li></a>

                        <a href="outras/comingsoon.html"><li class="h3 hvr-underline-from-left">Rastrear Serviço</li></a>
                    </ul>
                </div>
            </div>
        </div>
       
        <!menu pequeno>
        <div class="container-fluid fluid hidden-md hidden-lg
            hidden-sm">
            <div class="row">
                
                    <ul class="menutitulo">
                        <a href="#"><li class="h5 hvr-underline-from-left">Inicio</li></a>

                        <a href="#pe"><li class="h5 hvr-underline-from-left">Contato</li></a>

                        <a href="outras/comingsoon.html"><li class="h5 hvr-underline-from-left">Rastrear Serviço</li></a>
                    </ul>
                
            </div>
        </div><br>

                <div class="container">\n
                    <div class="row">\n
    \n
                            <div class="jumbotron  col-md-12" style="" >\n
                                <p class="h4">Dados do Cliente</p>\n
                                <hr>\n
                                <p class="h4">Nome: """ + nome + """ </p>\n
                                <p class="h4">ID: """ + client_id + """ </p>\n
                                <p class="h4">Início do Serviço: """+"0"+day+"/"+"0"+month+"/"+year+"""</p>\n
                            </div>\n    
                            <div class="jumbotron  col-md-12" style="" >\n
                                <p class="h4">Relatório do Serviço</p>\n
                                <hr>\n             
    \n                          <!ignit>
                                
                                <!done>    
                            </div>\n
                    </div>\n
                </div>\n
<div class=" col-xs-offset-4 col-sm-offset-5 col-md-offset-5"><a class="btn btn-default" href="../index.html" role="button">Voltar ao Site</a></div><br>\n
<footer class="container-fluid bg-4 text-center" id="pe">\n
            <div class="row">\n
                <!conttatos>\n
                <div class="text-left col-md-4 col-xs-12">\n
                    <p class="h3  animated pulse infinite">Contatos:</p>\n
                    <p class="h4"><i class="fa fa-whatsapp" aria-hidden="true"></i> (89) 999363289</p>\n
                    <p class="h5"><i class="fa fa-envelope-o" aria-hidden="true"></i> brunodonascimentomaciel@gmail.com</p>\n
                    <p class="h3 animated pulse infinite">Endereço:</p>\n
                    <p class="h4">Gilbués-PI, Av. Zeferino Vieira, Nº 289</p>\n
                </div>\n
                <!redes sociais>\n
                <div class="col-md-4 col-xs-12">\n
                    <p class=" h3">Redes Sociais</p>\n
                    <ul class="redes">\n
                        <li><a target="new_blank" href="https://www.facebook.com/Maciel-TI-Solu%C3%A7%C3%B5es-em-Inform%C3%A1tica-437373829932392/"><i class=" hvr-grow-rotate  fa fa-4x fa-facebook-official" aria-hidden="true"></i></a></li>\n
                        <li><a target="new_blank" href="https://www.youtube.com/channel/UCXPjcbGnBD5sEgQ2k3HNGWw"><i class="hvr-grow-rotate  fa fa-4x fa-youtube" aria-hidden="true"></i></a></li>\n
                    </ul>\n
                </div>\n
                \n
                <div class="col-md-4 col-xs-12">\n
                    <br><br>\n
                    <p class="h4 text-center" >Este site foi desenvolvido com muito <i class="fa fa-heart-o" aria-hidden="true"></i>, <i class="fa fa-coffee" aria-hidden="true"></i> e <i class="fa fa-music" aria-hidden="true"></i>. Por Bruno do Nascimento Maciel.</p>\n
                </div>    \n
                \n
            </div>\n
        </footer>\n
\n
            </body>\n
        </html>\n
    """)
    arq.close()

    ### Adição do If ao JS
    jsarq = open("configs/follow_service.js", "r")
    texto = jsarq.read()
    print (texto)
    jsarq.close()
    inicio = texto.find("//if")
    final =texto.find("//if_done")
    #abrindo o arquivo novamente para escrver a adição do if 
    jsarq = open("configs/follow_service.js", "w")
    jsarq.writelines(texto[:inicio+5]+ '''\n
//if_done\n
           if ( id == "'''+ client_id +'''") {\n
                window.location.assign("../clients/'''+client_id+'''.html'''+'''");\n
            }\n
    \n'''+ texto[final:])
    jsarq.close()
    #################
    ###atualizar o status de um serviço
if option =="2":
    client_id_att = input("Digite o ID do cliente:\n")
    atualizacao = input("Digite a atualização:\n")
    os.system("clear")
    arqclient = open("clients/"+client_id_att+".html", "r")
    html = arqclient.read()
    arqclient.close()
    #Data
    now = datetime.now()
    year= str(now.year)
    month= str(now.month)
    day= str(now.day)

    ignit = html.find("<!ignit>")
    done = html.find("<!done>")
    #escrever attualizaçao
    arqaddstaus = open("clients/"+client_id_att+".html", "w")
    arqaddstaus.writelines(html[:ignit+8]+"\n"+'''
<!ignit>\n
                      <p class="h4"> '''+"0"+day+"/"+"0"+month+"/"+year+" - "+atualizacao+''' </p>
<!done>\n
    ''' +html[done:])
    arqaddstaus.close()
