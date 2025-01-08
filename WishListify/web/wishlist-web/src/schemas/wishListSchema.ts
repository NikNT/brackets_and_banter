"use client";

import { z } from "zod";

export const wishListSchema = z.object({
  name: z.string().max(50, "Name must be less than 50 characters"),
  description: z.string(),
  priority: z.enum(["High", "Medium", "Low"]).default("Medium"),
});
