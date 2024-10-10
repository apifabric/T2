import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'LoyaltyProgram-new',
  templateUrl: './LoyaltyProgram-new.component.html',
  styleUrls: ['./LoyaltyProgram-new.component.scss']
})
export class LoyaltyProgramNewComponent {
  @ViewChild("LoyaltyProgramForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}