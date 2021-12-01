import { Component, OnInit } from '@angular/core';
import { EgresoServicio } from '../egreso/egreso.service';
import { Ingreso } from '../ingreso/ingreso.model';
import { IngresoServicio } from '../ingreso/ingreso.service';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css']
})
export class FormularioComponent implements OnInit {

  tipo: string;
  descripcionInput: string;
  valorInput: number;
  claseOperacion: string;

  constructor(private ingresoServicio: IngresoServicio,
              private egresoServicio: EgresoServicio) {
    this.tipo = "ingreso";
    this.claseOperacion = ""
  }

  ngOnInit(): void {
  }

  tipoOperacion(evento): void {
    this.tipo = evento.target.value;
  }

  agregarValor() : void {
    if (this.tipo === "ingreso") {
      this.ingresoServicio.ingresos.push(new Ingreso(this.descripcionInput, this.valorInput))
    } else { 
      this.egresoServicio.egresos.push(new Ingreso(this.descripcionInput, this.valorInput))
    }
  }

}
