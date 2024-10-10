import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './LoyaltyProgram-card.component.html',
  styleUrls: ['./LoyaltyProgram-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.LoyaltyProgram-card]': 'true'
  }
})

export class LoyaltyProgramCardComponent {


}