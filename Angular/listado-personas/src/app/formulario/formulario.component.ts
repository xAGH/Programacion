import { Component, ElementRef, ViewChild } from '@angular/core';
import { Persona } from '../persona.model';
import { PersonasService } from '../persona.service';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css'],
})
export class FormularioComponent {

  nombre: string;
  apellidos: string;

  constructor(private PersonasService: PersonasService) {
    this.PersonasService.saludar.subscribe((indice: number) => {
      alert("El indice es " + (indice + 1));
    })
  }

  agregarPersona(): void {
    let persona: Persona = new Persona(this.nombre, this.apellidos);
    this.PersonasService.agregarPersona(persona)
  };

}
