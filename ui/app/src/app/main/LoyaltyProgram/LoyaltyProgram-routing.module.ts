import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoyaltyProgramHomeComponent } from './home/LoyaltyProgram-home.component';
import { LoyaltyProgramNewComponent } from './new/LoyaltyProgram-new.component';
import { LoyaltyProgramDetailComponent } from './detail/LoyaltyProgram-detail.component';

const routes: Routes = [
  {path: '', component: LoyaltyProgramHomeComponent},
  { path: 'new', component: LoyaltyProgramNewComponent },
  { path: ':id', component: LoyaltyProgramDetailComponent,
    data: {
      oPermission: {
        permissionId: 'LoyaltyProgram-detail-permissions'
      }
    }
  }
];

export const LOYALTYPROGRAM_MODULE_DECLARATIONS = [
    LoyaltyProgramHomeComponent,
    LoyaltyProgramNewComponent,
    LoyaltyProgramDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LoyaltyProgramRoutingModule { }