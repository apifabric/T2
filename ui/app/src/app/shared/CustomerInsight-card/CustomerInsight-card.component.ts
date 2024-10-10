import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CustomerInsight-card.component.html',
  styleUrls: ['./CustomerInsight-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CustomerInsight-card]': 'true'
  }
})

export class CustomerInsightCardComponent {


}