import { Component, OnInit } from '@angular/core';
import { AdminService } from 'src/app/services/admin.service';

@Component({
  selector: 'app-admin-panel',
  templateUrl: './admin-panel.component.html',
  styleUrls: ['./admin-panel.component.css']
})
export class AdminPanelComponent implements OnInit {
  public file: File;

  constructor(public adminService: AdminService) { }

  ngOnInit(): void {
  }

  onFileSelected(event: any)
  {
    this.file = event.target.files[0];
    console.log(this.file)
  }

  uploadFile() {
    console.log(this.file)
    this.adminService.uploadFile(this.file).subscribe((data) => console.log(data))
  }
}
