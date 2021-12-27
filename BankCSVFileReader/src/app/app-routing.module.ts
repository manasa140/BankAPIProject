import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DataUploadComponent } from './data-upload/data-upload.component';
import { DataViewComponent } from './data-view/data-view.component';


const routes: Routes = [
  {path:'',component:DataUploadComponent},
  {path:'DataView',component:DataViewComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
