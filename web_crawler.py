# Pacotes



# Criar diretório da execução com uuid v7


# Ler urls configuradas para checagem (RF01)
# Iniciar a lista de endereços e a lista de endereços pendentes (RF02)


# INICIANDO WEB CRAWLER

    # Reservar as threadas e preparar os workers

    # Iniciar os workers
    # Para cada worker

        # Solicitar endereço pendente (RF02)

        # Realizar a requisição

        # Capturar a resposta

        # Identificar status HTTP da resposta (RF03)
            #Registrar caso seja 4xx ou 5xx

        # Varrer apenas o body da resposta buscando os links

        # Para cada link encontrado (RF02)
            # Solicitar a checagem se já foi inserido na lista de itens
            # Se não tiver sido, solicitar a inserção
            # Registrar link (origem e destino)

        # Repetir até não ter mais endereços pendentes

        # finalizar worker

    # finalizar checagem