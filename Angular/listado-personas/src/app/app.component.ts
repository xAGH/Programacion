import { Component } from '@angular/core';
import { Persona } from './persona.model'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  titulo: string;
  personas: Persona[];

  constructor() {
    this.titulo = 'Listado de personas';
    this.personas = [
      new Persona("Juan", "Peréz"),
      new Persona("Laura", "Juarez"),
      new Persona("Karla", "Lara")
    ];
  }

  personaAgregada(persona: Persona) : void {
    this.personas.push(persona);
  }
}
