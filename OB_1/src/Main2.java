public class Main2 {
    public static void main(String[] args){
        coche miCoche = new coche();
        miCoche.sumarPuerta();
        System.out.println("El coche tiene: "+ miCoche.puerta +" Puertas");
    }
       static class coche {
        public int puerta = 4;
                public void sumarPuerta(){
                    this.puerta++;
                }

        }
    }

