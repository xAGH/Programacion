import { Component, OnInit } from '@angular/core';
import { Persona } from './persona.model'
import { PersonasService } from './persona.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  
  titulo: string;
  personas: Persona[];

  constructor(private PersonasService: PersonasService) {
    this.titulo = 'Listado de personas';
  }
   
  ngOnInit(): void {
    this.personas = this.PersonasService.personas;
  }
}
