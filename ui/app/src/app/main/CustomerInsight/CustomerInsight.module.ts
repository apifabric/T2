import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CUSTOMERINSIGHT_MODULE_DECLARATIONS, CustomerInsightRoutingModule} from  './CustomerInsight-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CustomerInsightRoutingModule
  ],
  declarations: CUSTOMERINSIGHT_MODULE_DECLARATIONS,
  exports: CUSTOMERINSIGHT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CustomerInsightModule { }