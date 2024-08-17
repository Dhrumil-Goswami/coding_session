s = raw_input()
d={"DIGITS":0, "LETTERS":0}

for c in s:
    z=[]
    
    if (c.isdigit()):
        print c
        d["DIGITS"]+=1
    elif (c.isalpha()):
        print c
        
        d["LETTERS"]+=1
    else:
        pass

print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]
    


@api.multi
def action_view_button(self):
tree_view_id =self.env.ref('school.view_subject_tree').id
return {
'name':'Subject Tree View',
'type':'ir.actions.act_window',
'res_model':'subject.record',
'view_type': 'form',
'view_mode':'tree,form',
'views':[(tree_view_id,'tree'),(False,'form')],
'target':'current',
'domain': [('student_id', 'in', [self.id])],
'context': {'default_student_id': self.id},
}
