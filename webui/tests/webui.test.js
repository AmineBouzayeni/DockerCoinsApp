const app = require('../webui')
const request = require("supertest");

describe("GET /", () => {
    it("should return the UI", async () => {
      const res = await request(app).get("/");
      expect(res.statusCode).toBe(200);
    });
  });


describe("GET /json", () => {
    it("should return the mining details", async () => {
      const res = await request(app).get("/");
      expect(res.statusCode).toBe(200);
      expect(res.body.length).toBeGreaterThan(0);
    });
  });