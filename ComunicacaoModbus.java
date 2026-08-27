public class ComunicacaoModbus {
    public static void main(String[] args) {
        boolean eMestre = true;

        System.out.println("----------- Simulação da Comunicação Modbus -----");

        if (eMestre) {
            System.out.println("[Mestre]: Solicitando leitura do registrador do Transmissor de Nível (Escravo 1)...");
            System.out.println("[Escravo 1]: Resposta enviada com sucesso: 75.4 %");
        } else {
            System.out.println("[Escravo]: Aguardando requisição do Mestre....");
        }
    }
}
