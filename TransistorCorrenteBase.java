public class TransistorCorrenteBase {
    public static void main(String[] args) {
        double beta = 200.0;     // Ganho de corrente
        double iColetor = 10.0;  // Corrente de coletor em mA

        double iBase = iColetor / beta;

        System.out.printf("A corrente de base (IB) é: %.2f mA%n", iBase);
    }
}
