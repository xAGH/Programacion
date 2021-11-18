import { Component, OnInit } from '@angular/core';
import { Egreso } from './egreso/egreso.model';
import { EgresoServicio } from './egreso/egreso.service';
import { Ingreso } from './ingreso/ingreso.model';
import { IngresoServicio } from './ingreso/ingreso.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  ingresos: Ingreso[];

  egresos: Egreso[];

  constructor(private ingresoServicio: IngresoServicio,
              private egresoServicio: EgresoServicio) {}
  
  ngOnInit(): void {
    this.ingresos = this.ingresoServicio.ingresos;
    this.egresos = this.egresoServicio.egresos;
  }

  getIngresoTotal(): number{ 
    let ingresoTotal: number = 0;
    this.ingresos.forEach(ingreso => {
      ingresoTotal += ingreso.valor
    });
    return ingresoTotal;
  }

  getEgresoTotal(): number{ 
    let egresoTotal: number = 0;
    this.egresos.forEach(egreso => {
      egresoTotal += egreso.valor
    });
    return egresoTotal;
  }

  getPorcentajeTotal() : number {
    return this.getEgresoTotal() / this.getIngresoTotal();
  }

  getPresupuestoTotal() : number {
    return this.getIngresoTotal() - this.getEgresoTotal()
  }

}
