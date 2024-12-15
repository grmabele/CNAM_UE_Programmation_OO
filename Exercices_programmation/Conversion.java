import java.util.Scanner;

public class Conversion {
    public static void main(String[] args){

        // création du scanner pour lire l'entrer de l'utilisateur
        Scanner scanner = new Scanner(System.in);

        
        // demande à l'utilisateur de saisir la température
        System.out.print("Entrez une temperature en celsus : ");
        double celsus = scanner.nextDouble();

        // Conversion de la température en Fahrenheit
        double fahrenheit = (celsus * 9/5) + 32;

        // Affichage du résultat arrondi à deux décimales
        System.out.printf("La température équivalente en Fahrenheit est : %.2f°F%n", fahrenheit);

        // Fremeture du scanner
        scanner.close();
    }
}