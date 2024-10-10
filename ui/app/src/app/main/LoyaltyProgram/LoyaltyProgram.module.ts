import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {LOYALTYPROGRAM_MODULE_DECLARATIONS, LoyaltyProgramRoutingModule} from  './LoyaltyProgram-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    LoyaltyProgramRoutingModule
  ],
  declarations: LOYALTYPROGRAM_MODULE_DECLARATIONS,
  exports: LOYALTYPROGRAM_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class LoyaltyProgramModule { }