public class InstrumentacaoRangeSpan {
    public static void main(String[] args) {
        double valorInferior = -10.0; // LRV
        double valorSuperior = 90.0;  // URV

        double span = valorSuperior - valorInferior;

        System.out.printf("Faixa medida (Range): %.1f a %.1f%n", valorInferior, valorSuperior);
        System.out.printf("O Span do instrumento é: %.1f%n", span);
    }
}
