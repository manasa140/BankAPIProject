import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router, RouterModule, Routes } from '@angular/router';

@Component({
  selector: 'app-data-upload',
  templateUrl: './data-upload.component.html',
  styleUrls: ['./data-upload.component.css']
})
export class DataUploadComponent implements OnInit {
  message: any = null;
  selectedFile:any = null;
  msg : String = '';

  constructor(private http: HttpClient,private _router:Router) { } 
  onFileSelected(event:any){
    this.selectedFile = <File>event.target.files[0];
    console.log(event);
  }
  DataView(DataView:any)
  {
    this._router.navigate([DataView]);
  }
  onUpload(){
    const fd = new FormData();
    fd.append('file',this.selectedFile,this.selectedFile.name)
    this.http.post('http://127.0.0.1:5000/file',fd)
    .subscribe(res=>{
      console.log(res);
      this.message = res;
      this.msg = this.message.message;
    });
  }

  ngOnInit(): void {
  }

}
