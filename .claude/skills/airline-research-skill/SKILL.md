---
name: airline-research
description: "Research airlines to understand their current holiday platforms, partnerships, and ancillary strategies. Produces detailed research briefs that classify airlines into target scenarios and recommend approach angles for sales outreach."
---

# Airline Research Skill

Research airlines to create contextual, informed sales outreach.

## Purpose

Understand an airline's current situation before creating marketing materials:
- Holiday brand and booking capabilities
- Hotel/car rental partnerships
- Recent news on ancillary strategy
- Loyalty program scope
- Technology partners

Output: Detailed research brief with classification and recommended approach.

---

## Research Process

### Step 1: Receive Assignment

You will be asked to research a specific airline. Typical request format:
```
Research [Airline Name] for sales outreach.
Follow the airline-research methodology.
Save brief to output/research-[airline-slug]-[YYYYMMDD].md
Return: classification, key findings, recommended approach angle.
```

### Step 2: Web Search Intelligence

Execute 4 strategic searches using **mcp__web-search-prime__webSearchPrime**:

**Search 1: Holiday Brand Discovery**
- Query: `"[Airline] Holidays" OR "[Airline] vacation packages"`
- Look for: Official pages, branded products, press releases
- Goal: Does a branded holiday product exist?

**Search 2: Partnership Intelligence**
- Query: `"[Airline] hotel partnership" OR "[Airline] Booking.com" OR "[Airline] Expedia"`
- Look for: White-label deals, OTA partnerships, "powered by" mentions
- Goal: Who powers their hotel/car sections?

**Search 3: Non-Air Ancillary Strategy**
- Query: `"[Airline] non-air ancillary" OR "[Airline] ancillary revenue strategy 2026"`
- Look for: Executive quotes, investor presentations, strategy announcements
- Goal: What's their current ancillary focus?

**Search 4: Loyalty & Travel Products**
- Query: `"[Airline] [loyalty program name] redemption hotels" OR "[Airline] frequent flyer travel products"`
- Look for: Redemption options, travel marketplace, partner programs
- Goal: What non-flight products can members redeem for?

### Step 3: Website Deep Dive

Use **mcp__web-reader__webReader** to inspect:

**1. Home Country Site (in English)**

Construct URL using home country domain:
- Lufthansa: `lufthansa.com/de/en`
- Qatar Airways: `qatarairways.com/en-qa/homepage.html`
- Ethiopian Airlines: `ethiopianairlines.com`
- Malaysia Airlines: `malaysiaairlines.com/my/en.html`
- Air France: `airfrance.com/fr/en`

**2. Holiday Platform Inspection (if found)**

If a holiday/packages website exists:
- Visit the holiday platform
- Browse to a sample package/destination
- **CRITICAL:** Click "Book Now" or equivalent CTA
- Examine the booking flow carefully

**3. Site Search Verification**

Use the airline's main website search function:
- Search for: "holidays", "stopover", "hotel", "vacation packages"
- Note if results are found or "0 results"
- Verify products are actively promoted (not just old pages)

### Step 4: Booking Capability Verification

**This is critical - don't trust appearances. Test the actual flow.**

**Red flags = Enquiry-only (NO real booking engine):**
- ❌ "Contact us for pricing"
- ❌ "Request a quote" or "Enquiry form"
- ❌ Form asks for "preferred dates" (not actual availability)
- ❌ No prices displayed on packages
- ❌ No payment gateway visible
- ❌ Email-only contact (e.g., "email holidays@airline.com")
- ❌ Submission sends an enquiry, not a booking

**Green flags = Real booking engine:**
- ✅ Calendar with actual availability
- ✅ Prices displayed in real-time
- ✅ Passenger details collection (names, passport info)
- ✅ Payment integration (credit card form, payment gateway)
- ✅ Instant confirmation / booking reference number
- ✅ Can complete transaction end-to-end online

**Example of enquiry-only:**
- Ethiopian Holidays: https://www.ethiopianholidays.com/packages/enquire/qkwa9gno
- Looks professional but clicking "Book Now" → enquiry form → email sent

### Step 5: Classify Airline

Based on findings, classify into one of these scenarios:

**A1 - Brand + Content, NO Tech** ⭐⭐⭐ **PRIME TARGET**
- Has holiday brand with content
- Booking flow = enquiry form only (no real booking engine)
- **Approach:** "You've built the brand - add the tech to make it transactional"
- **Example:** Ethiopian Holidays

**A2 - Full Holiday Platform** ⭐
- Has holiday brand + full booking engine with payment
- Real-time availability, pricing, instant confirmation
- **Approach:** "Expand globally" or "Upgrade technology"

**B - OTA White-Label** ⭐⭐
- Hotel section powered by Booking.com/Expedia/similar
- May be integrated or iframe
- **Approach:** "Own the customer journey, don't hand off to OTA"

**C - Affiliate Links Only** ⭐⭐
- "Hotels" section exists but redirects to external site
- No integration, just referral links
- **Approach:** "Capture revenue you're currently losing"

**D - No Holiday Offering** ⭐⭐⭐
- No hotel/holiday section found
- No branded holiday product
- **Approach:** "Untapped revenue opportunity"

**E - Insufficient Data**
- Research inconclusive
- Limited public information
- **Approach:** Neutral industry problem statement

### Step 6: Save Research Brief

Create file: `output/research-[airline-slug]-[YYYYMMDD].md`

Use this template:

```markdown
# [Airline Name] - Research Brief
**Date:** DD/MM/YYYY
**Researcher:** airline-research agent
**Research Duration:** ~X minutes

## Executive Summary

[2-3 sentence overview of current state]

**Target Classification:** [Scenario] - [Description]

---

## Holiday Brand & Offerings

**Status:** [Has/Doesn't have] holiday platform
**Brand name:** [Name] / None
**Website:** [URL] / None
**Product type:** [Full booking engine / Enquiry-only / None]

### [If applicable] CRITICAL FINDING: No Booking Engine

**What they have:**
- [List content, branding, packages]

**What they DON'T have:**
- ❌ Real-time booking engine
- ❌ Dynamic pricing
- ❌ [Other missing capabilities]

**Booking process reality:**
1. [Describe actual flow]
2. [What happens when user clicks "Book Now"]

**Evidence:** [URLs]

### Site Search Verification

**Test performed:** Searched "[term]" on [airline].com main search
- **Result:** [X results found / 0 results]

**Conclusion:** [Integration status]

---

## Technology Partners

**Hotel provider:** [Partner name] / None
**Car rental:** [Partner name] / None
**Activities/Tours:** [Partner name] / None

**Recent Technology Partnerships:**
1. **[Partner Name]** ([Date])
   - [What they do]
   - [Relevance to non-air ancillaries]

**Pattern observed:** [e.g., All air-focused, no non-air investment]

**Evidence:** [URLs]

---

## Loyalty & Redemption

**Loyalty Program:** [Name]
**Hotel redemption:** Yes / No / Unknown
**Earn rate:** [X miles per $]

**Non-Air Products:**
- [List redemption options]

**Evidence:** [URLs]

---

## Recent News & Strategy

**Major Theme:** [Strategic focus]

**Key Announcements:**
1. **[Title]** ([Date])
   - [Summary]
   - [Relevance quote]

**Executive Language:**
- "[Quote about strategy]"
- "[Quote about priorities]"

**Critical Gap:** [What they're NOT investing in]

**Evidence:** [URLs]

---

## Recommended Approach Angle

**Target Classification:** [Scenario] ⭐⭐⭐ [Rating]

**Primary Hook:**
> "[Opening line that references their specific situation]"

**Value Proposition:**
- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

**Proof Points to Use:**
- **Primary:** [Most relevant customer]
- **Secondary:** [Alternative proof point]

**What to Avoid:**
- ❌ [Don't mention X]
- ❌ [Don't criticize Y]

**Key Differentiators:**
1. [Why this matters to them]
2. [Strategic alignment]

---

## Proposed Email Subject Lines

1. **Direct:** "[Subject based on findings]"
2. **Timely:** "[Subject using recent news]"
3. **Strategic:** "[Subject aligned with their goals]"

---

## Source URLs

**Official Sites:**
- [List all airline URLs visited]

**Press Releases:**
- [List corporate/news URLs]

**Industry News:**
- [List third-party news coverage]

**Verification:**
- [List URLs used for testing/verification]

---

## Next Steps

1. Draft personalized sales email referencing [specific findings]
2. Prepare supporting materials: [relevant case studies]
3. Target contacts: [suggested roles]
```

### Step 7: Return Summary

After saving the research brief, return a concise summary to the requesting agent:

```
Research complete for [Airline Name].

Classification: [Scenario] - [Rating]

Key findings:
- [Finding 1]
- [Finding 2]
- [Finding 3]

Recommended approach: [Primary hook]

Proof points: [Relevant customers]

Research brief saved to: output/research-[airline-slug]-[YYYYMMDD].md
```

---

## Quality Checklist

Before finalizing research, verify:

- [ ] Did I test the booking flow (not just trust web search results)?
- [ ] Did I use site search to verify active promotion?
- [ ] Are findings from official sources (last 12-24 months)?
- [ ] Have I identified a specific strategic gap or opportunity?
- [ ] Can I reference something specific about THIS airline (not generic trends)?
- [ ] Is the classification accurate based on actual testing?
- [ ] Did I save the brief with correct filename format?
- [ ] Does my summary give the main agent what they need to write?

---

## Common Patterns to Look For

**Airlines with brand but no tech (A1):**
- Professional website with package descriptions
- "Contact us" or "Request quote" as primary CTA
- Email address like "holidays@airline.com"
- Manual inquiry process

**Airlines with OTA white-label (B):**
- "Powered by Booking.com" in footer
- Hotel section iframed from external site
- Redirects to OTA for completion

**Airlines with no offering (D):**
- No mention of hotels/holidays in main navigation
- Site search returns 0 results
- Only flight booking visible

---

## Regional Site Strategy

**Why home country site matters:**
- Airlines often launch holidays in home market first
- Regional sites may have different offerings
- English version of home country site shows their primary market

**How to find it:**
- Check airline's Wikipedia page for headquarters country
- Construct URL: `[airline].com/[country-code]/en`
- Examples:
  - Singapore Airlines (SG): singaporeair.com/en_UK/sg/home (but check singaporeair.com/en_UK/global)
  - Thai Airways (TH): thaiairways.com/en_TH/index.page
  - Qantas (AU): qantas.com/au/en.html

---

## Time Budget

**Estimated research time per airline:**
- 4 web searches: ~2-3 minutes
- Website inspection (3-4 pages): ~2-3 minutes
- Booking flow testing: ~1-2 minutes
- Site search verification: ~1 minute
- Classification & synthesis: ~1-2 minutes
- Writing brief: ~3-5 minutes

**Total: 10-15 minutes per airline**

This is thorough enough for contextual outreach without excessive time investment.

---

## Example Research Outputs

See `output/research-ethiopian-airlines-20260104.md` for a complete example of:
- A1 classification (brand + content, no tech)
- Booking flow verification
- Technology partnership analysis
- Recommended approach angles
