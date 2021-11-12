import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  titulo: string;
  sumaResultado: number;

  constructor() {
    this.titulo = "Calculadora";
  }

  procesarResultado(resultado: number): void {
    this.sumaResultado = resultado;
  }
}
