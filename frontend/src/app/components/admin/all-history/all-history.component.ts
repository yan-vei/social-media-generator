import { Component, OnInit } from '@angular/core';
import { AdminService } from 'src/app/services/admin.service';

@Component({
  selector: 'all-history',
  templateUrl: './all-history.component.html',
  styleUrls: ['./all-history.component.css']
})
export class AllHistoryComponent implements OnInit {

  constructor(private adminService: AdminService) { }

  ngOnInit(): void {
  }

}
