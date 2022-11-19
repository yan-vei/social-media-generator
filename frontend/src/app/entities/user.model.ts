export class User {
  constructor(
    public username: string,
    public email: string,
    public password: string,
    public id?: number,
    public registered_on?: Date
  ) {}
}
