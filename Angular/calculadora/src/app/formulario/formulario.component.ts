import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css']
})
export class FormularioComponent {

  num1: number;
  num2: number;
  @Output() suma: EventEmitter<number> = new EventEmitter<number>();

  sumar(): void {
    this.suma.emit(this.num1 + this.num2);
  }

  constructor() {}

}
