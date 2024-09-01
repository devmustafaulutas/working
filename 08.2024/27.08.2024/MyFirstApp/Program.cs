using System;

    namespace Program {
        class MyApp{
            static void Main(string[] args)
            {
                Console.WriteLine("Adınızı giriniz: ");
                String name = Console.ReadLine();
                Console.WriteLine($"{name} selam! Nasılsın?");
                
            }
        }
    }