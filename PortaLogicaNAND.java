public class PortaLogicaNAND {
    public static void main(String[] args) {
        int[][] combinacoes = {
            {0, 0, 0},
            {0, 0, 1},
            {0, 1, 1},
            {1, 1, 1},
            {1, 0, 1}
        };

        System.out.println("J | L | M | Saída X");
        System.out.println("-----------");
        for (int[] combo : combinacoes) {
            int j = combo[0];
            int l = combo[1];
            int m = combo[2];

            boolean saidaAND = (j == 1) && (l == 1);
            boolean saidaX = !(saidaAND && (m == 1));
            int resultadoX = saidaX ? 1 : 0;

            System.out.printf("%d | %d | %d |   %d%n", j, l, m, resultadoX);
        }
    }
}
