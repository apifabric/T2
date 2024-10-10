import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CustomerInsightHomeComponent } from './home/CustomerInsight-home.component';
import { CustomerInsightNewComponent } from './new/CustomerInsight-new.component';
import { CustomerInsightDetailComponent } from './detail/CustomerInsight-detail.component';

const routes: Routes = [
  {path: '', component: CustomerInsightHomeComponent},
  { path: 'new', component: CustomerInsightNewComponent },
  { path: ':id', component: CustomerInsightDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CustomerInsight-detail-permissions'
      }
    }
  }
];

export const CUSTOMERINSIGHT_MODULE_DECLARATIONS = [
    CustomerInsightHomeComponent,
    CustomerInsightNewComponent,
    CustomerInsightDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CustomerInsightRoutingModule { }