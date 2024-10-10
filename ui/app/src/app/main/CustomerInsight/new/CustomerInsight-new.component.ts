import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CustomerInsight-new',
  templateUrl: './CustomerInsight-new.component.html',
  styleUrls: ['./CustomerInsight-new.component.scss']
})
export class CustomerInsightNewComponent {
  @ViewChild("CustomerInsightForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}