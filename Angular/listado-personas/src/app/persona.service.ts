import { EventEmitter, Injectable } from "@angular/core";
import { LogginService } from "./loggin.service";
import { Persona } from "./persona.model";

@Injectable()
export class PersonasService {

    personas: Persona[];
    saludar: EventEmitter<number>;

    constructor (private logginService: LogginService) {
        this.personas = [
            new Persona("Juan", "Peréz"),
            new Persona("Laura", "Juarez")
        ];
        this.saludar = new EventEmitter<number>();
    }

    agregarPersona(persona: Persona) : void {
        this.logginService.enviaMensajeAConsola("Agregamos persona: " + persona.nombre)
        this.personas.push(persona);
    }
}